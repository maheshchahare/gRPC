import time
import grpc

from concurrent.futures import ThreadPoolExecutor

import multiply_pb2
import multiply_pb2_grpc


TOTAL_REQUESTS = 100

MAX_WORKERS = 20


channel = grpc.insecure_channel("localhost:50051")

stub = multiply_pb2_grpc.ChatBotStub(channel)


def send_request(request_number):

    start = time.time()

    request = multiply_pb2.ChatRequest(message="""hi""")

    responses = stub.Chat(request)

    result = ""

    for response in responses:
        result += response.reply

    end = time.time()

    latency = end - start

    # print(f"gRPC Request {request_number} completed in {latency:.4f} sec")

    return latency


overall_start = time.time()

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    latencies = list(executor.map(send_request, range(TOTAL_REQUESTS)))

overall_end = time.time()

print("\n========== gRPC RESULTS ==========")

print(f"Total Requests: {TOTAL_REQUESTS}")

print(f"Total Time: {overall_end - overall_start:.2f} sec")

print(f"Average Latency: {sum(latencies) / len(latencies):.4f} sec")
