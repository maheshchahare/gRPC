import time
import requests

from concurrent.futures import ThreadPoolExecutor


URL = "http://localhost:8000/chat"

TOTAL_REQUESTS = 100

MAX_WORKERS = 20


def send_request(request_number):

    start = time.time()

    response = requests.post(
        URL,
        json={"message": """hi"""},
    )

    end = time.time()

    latency = end - start

    # print(f"REST Request {request_number} completed in {latency:.4f} sec")

    return latency


overall_start = time.time()

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    latencies = list(executor.map(send_request, range(TOTAL_REQUESTS)))

overall_end = time.time()

print("\n========== REST RESULTS ==========")

print(f"Total Requests: {TOTAL_REQUESTS}")

print(f"Total Time: {overall_end - overall_start:.2f} sec")

print(f"Average Latency: {sum(latencies) / len(latencies):.4f} sec")
