# compare.py

import time
import grpc
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from concurrent.futures import ThreadPoolExecutor

import multiply_pb2
import multiply_pb2_grpc

# ==========================================

# CONFIGURATION

# ==========================================

TOTAL_REQUESTS_LIST = [100, 500, 1000, 5000, 10000]

WORKERS_LIST = [20, 100, 200, 500, 1000]

REST_URL = "http://localhost:8000/chat"

# ==========================================

# gRPC CHANNEL

# ==========================================

grpc_channel = grpc.insecure_channel("localhost:50051")

grpc_stub = multiply_pb2_grpc.ChatBotStub(grpc_channel)

# ==========================================

# RESULTS STORAGE

# ==========================================

results = []

# ==========================================

# REST REQUEST

# ==========================================


def rest_request(_):

    start = time.time()

    response = requests.post(REST_URL, json={"message": "hi"})

    response.text

    end = time.time()

    latency = end - start

    return latency


# ==========================================

# gRPC REQUEST

# ==========================================


def grpc_request(_):

    start = time.time()

    request = multiply_pb2.ChatRequest(message="hi")

    responses = grpc_stub.Chat(request)

    result = ""

    for response in responses:
        result += response.reply

    end = time.time()

    latency = end - start

    return latency


# ==========================================

# METRIC CALCULATOR

# ==========================================


def calculate_metrics(latencies, total_time):

    avg_duration = np.mean(latencies)

    throughput = len(latencies) / total_time

    p95_latency = np.percentile(latencies, 95)

    return {
        "total_time": total_time,
        "avg_duration": avg_duration,
        "throughput": throughput,
        "p95_latency": p95_latency,
    }


# ==========================================

# MAIN BENCHMARK LOOP

# ==========================================

for total_requests, workers in zip(TOTAL_REQUESTS_LIST, WORKERS_LIST):
    print("\n====================================")
    print(f"Running Benchmark Requests={total_requests}, Workers={workers}")
    print("====================================")

    # ======================================
    # REST BENCHMARK
    # ======================================

    rest_start = time.time()

    with ThreadPoolExecutor(max_workers=workers) as executor:
        rest_latencies = list(executor.map(rest_request, range(total_requests)))

    rest_total_time = time.time() - rest_start

    rest_metrics = calculate_metrics(rest_latencies, rest_total_time)

    # ======================================
    # gRPC BENCHMARK
    # ======================================

    grpc_start = time.time()

    with ThreadPoolExecutor(max_workers=workers) as executor:
        grpc_latencies = list(executor.map(grpc_request, range(total_requests)))

    grpc_total_time = time.time() - grpc_start

    grpc_metrics = calculate_metrics(grpc_latencies, grpc_total_time)

    # ======================================
    # STORE RESULTS
    # ======================================

    results.append(
        {
            "requests": total_requests,
            "workers": workers,
            # REST Metrics
            "rest_total_time": rest_metrics["total_time"],
            "rest_avg_duration": rest_metrics["avg_duration"],
            "rest_throughput": rest_metrics["throughput"],
            "rest_p95_latency": rest_metrics["p95_latency"],
            # gRPC Metrics
            "grpc_total_time": grpc_metrics["total_time"],
            "grpc_avg_duration": grpc_metrics["avg_duration"],
            "grpc_throughput": grpc_metrics["throughput"],
            "grpc_p95_latency": grpc_metrics["p95_latency"],
        }
    )

# ==========================================

# CREATE DATAFRAME

# ==========================================

df = pd.DataFrame(results)

print("\n====================================")
print("FINAL RESULTS")
print("====================================")

print(df)

# ==========================================

# SAVE CSV

# ==========================================

df.to_csv("results.csv", index=False)

print("\nresults.csv saved successfully")

# ==========================================

# GRAPH 1

# TOTAL TIME

# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(df["requests"], df["rest_total_time"], marker="o", label="REST")

plt.plot(df["requests"], df["grpc_total_time"], marker="o", label="gRPC")

plt.xlabel("Total Requests")

plt.ylabel("Total Time (sec)")

plt.title("REST vs gRPC - Total Time")

plt.legend()

plt.grid(True)

plt.show()

# ==========================================

# GRAPH 2

# AVG REQUEST DURATION

# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(df["requests"], df["rest_avg_duration"], marker="o", label="REST")

plt.plot(df["requests"], df["grpc_avg_duration"], marker="o", label="gRPC")

plt.xlabel("Total Requests")

plt.ylabel("Average Request Duration (sec)")

plt.title("REST vs gRPC - Avg Request Duration")

plt.legend()

plt.grid(True)

plt.show()

# ==========================================

# GRAPH 3

# THROUGHPUT

# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(df["requests"], df["rest_throughput"], marker="o", label="REST")

plt.plot(df["requests"], df["grpc_throughput"], marker="o", label="gRPC")

plt.xlabel("Total Requests")

plt.ylabel("Requests Per Second")

plt.title("REST vs gRPC - Throughput")

plt.legend()

plt.grid(True)

plt.show()

# ==========================================

# GRAPH 4

# P95 LATENCY

# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(df["requests"], df["rest_p95_latency"], marker="o", label="REST")

plt.plot(df["requests"], df["grpc_p95_latency"], marker="o", label="gRPC")

plt.xlabel("Total Requests")

plt.ylabel("P95 Latency (sec)")

plt.title("REST vs gRPC - P95 Latency")

plt.legend()

plt.grid(True)

plt.show()
