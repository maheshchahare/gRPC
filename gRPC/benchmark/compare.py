import time
import grpc
import requests
import pandas as pd
import matplotlib.pyplot as plt

from concurrent.futures import ThreadPoolExecutor

import multiply_pb2
import multiply_pb2_grpc


TOTAL_REQUESTS_LIST = [100, 500, 1000, 5000, 10000]

WORKERS_LIST = [20, 100, 200, 500, 1000]


grpc_channel = grpc.insecure_channel("localhost:50051")

grpc_stub = multiply_pb2_grpc.ChatBotStub(grpc_channel)


REST_URL = "http://localhost:8000/chat"


results = []


def grpc_request(_):

    request = multiply_pb2.ChatRequest(message="hi")

    responses = grpc_stub.Chat(request)

    result = ""

    for response in responses:
        result += response.reply

    return result


def rest_request(_):

    response = requests.post(REST_URL, json={"message": "hi"})

    return response.text


for total_requests, workers in zip(TOTAL_REQUESTS_LIST, WORKERS_LIST):
    print(f"\nRunning test: Requests={total_requests}, Workers={workers}")

    # REST Benchmark

    start = time.time()

    with ThreadPoolExecutor(max_workers=workers) as executor:
        list(executor.map(rest_request, range(total_requests)))

    rest_time = time.time() - start

    # gRPC Benchmark

    start = time.time()

    with ThreadPoolExecutor(max_workers=workers) as executor:
        list(executor.map(grpc_request, range(total_requests)))

    grpc_time = time.time() - start

    results.append(
        {
            "requests": total_requests,
            "workers": workers,
            "rest_time": rest_time,
            "grpc_time": grpc_time,
        }
    )


df = pd.DataFrame(results)

print(df)

df.to_csv("results.csv", index=False)


# Plot Graph

plt.figure(figsize=(10, 6))

plt.plot(df["requests"], df["rest_time"], marker="o", label="REST")

plt.plot(df["requests"], df["grpc_time"], marker="o", label="gRPC")

plt.xlabel("Total Requests")

plt.ylabel("Total Time (sec)")

plt.title("REST vs gRPC Performance")

plt.legend()

plt.grid(True)

plt.show()
