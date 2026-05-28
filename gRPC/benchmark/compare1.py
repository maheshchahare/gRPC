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

WORKERS_LIST = [20, 30, 50, 100, 200]

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

    try:
        start = time.time()

        response = requests.post(
            REST_URL,
            json={
                "message": """Praise for Hands-On Large Language Models
This is an exceptional guide to the world of language models and their
practical applications in industry. Its highly-visual coverage of
generative, representational, and retrieval applications of language
models empowers readers to quickly understand, use, and refine LLMs.
Highly recommended!
—Nils Reimers, Director of Machine Learning at Cohere |
creator of sentence-transformers
Jay and Maarten have continued their tradition of providing beautifully
illustrated and insightful descriptions of complex topics in their new
book. Bolstered with working code, timelines, and references to key
papers, their book is a valuable resource for anyone looking to
understand the main techniques behind how Large Language Models are
built.
—Andrew Ng, founder of DeepLearning.AI
I can’t think of another book that is more important to read right now. On
every single page, I learned something that is critical to success in this
era of language models.
—Josh Starmer, StatQuest
If you’re looking to get up to speed in everything regarding LLMs, look
no further! In this wonderful book, Jay and Maarten will take you from
zero to expert in the history and latest advances in large language
models. With very intuitive explanations, great real-life examples, clear
illustrations, and comprehensive code labs, this book lifts the curtain on
the complexities of transformer models, tokenizers, semantic search,
RAG, and many other cutting-edge technologies. A must read for anyone
interested in the latest AI technology!
—Luis Serrano, PhD, Founder and CEO of Serrano
Academy
This book is a must-read for anyone interested in the rapidly-evolving
field of generative AI. With a focus on both text and visual embeddings,
it’s a great blend of algorithmic evolution, theoretical rigor, and practical
guidance. Whether you are a student, researcher, or industry
professional, this book will equip you with the use cases and solutions
needed to level-up your knowledge of generative AI. Well done!
—Chris Fregly, Principal Solution Architect, Generative
AI at AWS
In the heart of the GenAI revolution, this indispensable guide masterfully
balances theory and practice, navigating the vast landscape of large
language models to equip readers with the knowledge needed for
immediate and transformative impact in the field of AI.
—Tarun Narayanan Venkatachalam, AI Researcher,
University of Washington
Timely reading to get hands-on experience with language models.
—Emir Muñoz, Genesys
Hands-On Large Language Models brings clarity and practical examples
to cut through the hype of AI. It provides a wealth of great diagrams and
visual aids to supplement the clear explanations. The worked examples
and code make concrete what other books leave abstract. The book starts
with simple introductory beginnings, and steadily builds in scope. By the
final chapters, you will be fine-tuning and building your own large
language models with confidence.
—Leland McInnes, Researcher at the Tutte Institute for
Mathematics and Computing
Praise for Hands-On Large Language Models
This is an exceptional guide to the world of language models and their
practical applications in industry. Its highly-visual coverage of
generative, representational, and retrieval applications of language
models empowers readers to quickly understand, use, and refine LLMs.
Highly recommended!
—Nils Reimers, Director of Machine Learning at Cohere |
creator of sentence-transformers
Jay and Maarten have continued their tradition of providing beautifully
illustrated and insightful descriptions of complex topics in their new
book. Bolstered with working code, timelines, and references to key
papers, their book is a valuable resource for anyone looking to
understand the main techniques behind how Large Language Models are
built.
—Andrew Ng, founder of DeepLearning.AI
I can’t think of another book that is more important to read right now. On
every single page, I learned something that is critical to success in this
era of language models.
—Josh Starmer, StatQuest
If you’re looking to get up to speed in everything regarding LLMs, look
no further! In this wonderful book, Jay and Maarten will take you from
zero to expert in the history and latest advances in large language
models. With very intuitive explanations, great real-life examples, clear
illustrations, and comprehensive code labs, this book lifts the curtain on
the complexities of transformer models, tokenizers, semantic search,
RAG, and many other cutting-edge technologies. A must read for anyone
interested in the latest AI technology!
—Luis Serrano, PhD, Founder and CEO of Serrano
Academy
This book is a must-read for anyone interested in the rapidly-evolving
field of generative AI. With a focus on both text and visual embeddings,
it’s a great blend of algorithmic evolution, theoretical rigor, and practical
guidance. Whether you are a student, researcher, or industry
professional, this book will equip you with the use cases and solutions
needed to level-up your knowledge of generative AI. Well done!
—Chris Fregly, Principal Solution Architect, Generative
AI at AWS
In the heart of the GenAI revolution, this indispensable guide masterfully
balances theory and practice, navigating the vast landscape of large
language models to equip readers with the knowledge needed for
immediate and transformative impact in the field of AI.
—Tarun Narayanan Venkatachalam, AI Researcher,
University of Washington
Timely reading to get hands-on experience with language models.
—Emir Muñoz, Genesys
Hands-On Large Language Models brings clarity and practical examples
to cut through the hype of AI. It provides a wealth of great diagrams and
visual aids to supplement the clear explanations. The worked examples
and code make concrete what other books leave abstract. The book starts
with simple introductory beginnings, and steadily builds in scope. By the
final chapters, you will be fine-tuning and building your own large
language models with confidence.
—Leland McInnes, Researcher at the Tutte Institute for
Mathematics and Computing
Praise for Hands-On Large Language Models
This is an exceptional guide to the world of language models and their
practical applications in industry. Its highly-visual coverage of
generative, representational, and retrieval applications of language
models empowers readers to quickly understand, use, and refine LLMs.
Highly recommended!
—Nils Reimers, Director of Machine Learning at Cohere |
creator of sentence-transformers
Jay and Maarten have continued their tradition of providing beautifully
illustrated and insightful descriptions of complex topics in their new
book. Bolstered with working code, timelines, and references to key
papers, their book is a valuable resource for anyone looking to
understand the main techniques behind how Large Language Models are
built.
—Andrew Ng, founder of DeepLearning.AI
I can’t think of another book that is more important to read right now. On
every single page, I learned something that is critical to success in this
era of language models.
—Josh Starmer, StatQuest
If you’re looking to get up to speed in everything regarding LLMs, look
no further! In this wonderful book, Jay and Maarten will take you from
zero to expert in the history and latest advances in large language
models. With very intuitive explanations, great real-life examples, clear
illustrations, and comprehensive code labs, this book lifts the curtain on
the complexities of transformer models, tokenizers, semantic search,
RAG, and many other cutting-edge technologies. A must read for anyone
interested in the latest AI technology!
—Luis Serrano, PhD, Founder and CEO of Serrano
Academy
This book is a must-read for anyone interested in the rapidly-evolving
field of generative AI. With a focus on both text and visual embeddings,
it’s a great blend of algorithmic evolution, theoretical rigor, and practical
guidance. Whether you are a student, researcher, or industry
professional, this book will equip you with the use cases and solutions
needed to level-up your knowledge of generative AI. Well done!
—Chris Fregly, Principal Solution Architect, Generative
AI at AWS
In the heart of the GenAI revolution, this indispensable guide masterfully
balances theory and practice, navigating the vast landscape of large
language models to equip readers with the knowledge needed for
immediate and transformative impact in the field of AI.
—Tarun Narayanan Venkatachalam, AI Researcher,
University of Washington
Timely reading to get hands-on experience with language models.
—Emir Muñoz, Genesys
Hands-On Large Language Models brings clarity and practical examples
to cut through the hype of AI. It provides a wealth of great diagrams and
visual aids to supplement the clear explanations. The worked examples
and code make concrete what other books leave abstract. The book starts
with simple introductory beginnings, and steadily builds in scope. By the
final chapters, you will be fine-tuning and building your own large
language models with confidence.
—Leland McInnes, Researcher at the Tutte Institute for
Mathematics and Computing
Praise for Hands-On Large Language Models
This is an exceptional guide to the world of language models and their
practical applications in industry. Its highly-visual coverage of
generative, representational, and retrieval applications of language
models empowers readers to quickly understand, use, and refine LLMs.
Highly recommended!
—Nils Reimers, Director of Machine Learning at Cohere |
creator of sentence-transformers
Jay and Maarten have continued their tradition of providing beautifully
illustrated and insightful descriptions of complex topics in their new
book. Bolstered with working code, timelines, and references to key
papers, their book is a valuable resource for anyone looking to
understand the main techniques behind how Large Language Models are
built.
—Andrew Ng, founder of DeepLearning.AI
I can’t think of another book that is more important to read right now. On
every single page, I learned something that is critical to success in this
era of language models.
—Josh Starmer, StatQuest
If you’re looking to get up to speed in everything regarding LLMs, look
no further! In this wonderful book, Jay and Maarten will take you from
zero to expert in the history and latest advances in large language
models. With very intuitive explanations, great real-life examples, clear
illustrations, and comprehensive code labs, this book lifts the curtain on
the complexities of transformer models, tokenizers, semantic search,
RAG, and many other cutting-edge technologies. A must read for anyone
interested in the latest AI technology!
—Luis Serrano, PhD, Founder and CEO of Serrano
Academy
This book is a must-read for anyone interested in the rapidly-evolving
field of generative AI. With a focus on both text and visual embeddings,
it’s a great blend of algorithmic evolution, theoretical rigor, and practical
guidance. Whether you are a student, researcher, or industry
professional, this book will equip you with the use cases and solutions
needed to level-up your knowledge of generative AI. Well done!
—Chris Fregly, Principal Solution Architect, Generative
AI at AWS
In the heart of the GenAI revolution, this indispensable guide masterfully
balances theory and practice, navigating the vast landscape of large
language models to equip readers with the knowledge needed for
immediate and transformative impact in the field of AI.
—Tarun Narayanan Venkatachalam, AI Researcher,
University of Washington
Timely reading to get hands-on experience with language models.
—Emir Muñoz, Genesys
Hands-On Large Language Models brings clarity and practical examples
to cut through the hype of AI. It provides a wealth of great diagrams and
visual aids to supplement the clear explanations. The worked examples
and code make concrete what other books leave abstract. The book starts
with simple introductory beginnings, and steadily builds in scope. By the
final chapters, you will be fine-tuning and building your own large
language models with confidence.
—Leland McInnes, Researcher at the Tutte Institute for
Mathematics and Computing"""
            },
            timeout=30,
        )

        end = time.time()

        latency = end - start

        success = response.status_code == 200

        return latency, success

    except Exception as e:
        return None, False


# ==========================================

# gRPC REQUEST

# ==========================================


def grpc_request(_):

    try:
        start = time.time()

        request = multiply_pb2.ChatRequest(
            message="""Praise for Hands-On Large Language Models
This is an exceptional guide to the world of language models and their
practical applications in industry. Its highly-visual coverage of
generative, representational, and retrieval applications of language
models empowers readers to quickly understand, use, and refine LLMs.
Highly recommended!
—Nils Reimers, Director of Machine Learning at Cohere |
creator of sentence-transformers
Jay and Maarten have continued their tradition of providing beautifully
illustrated and insightful descriptions of complex topics in their new
book. Bolstered with working code, timelines, and references to key
papers, their book is a valuable resource for anyone looking to
understand the main techniques behind how Large Language Models are
built.
—Andrew Ng, founder of DeepLearning.AI
I can’t think of another book that is more important to read right now. On
every single page, I learned something that is critical to success in this
era of language models.
—Josh Starmer, StatQuest
If you’re looking to get up to speed in everything regarding LLMs, look
no further! In this wonderful book, Jay and Maarten will take you from
zero to expert in the history and latest advances in large language
models. With very intuitive explanations, great real-life examples, clear
illustrations, and comprehensive code labs, this book lifts the curtain on
the complexities of transformer models, tokenizers, semantic search,
RAG, and many other cutting-edge technologies. A must read for anyone
interested in the latest AI technology!
—Luis Serrano, PhD, Founder and CEO of Serrano
Academy
This book is a must-read for anyone interested in the rapidly-evolving
field of generative AI. With a focus on both text and visual embeddings,
it’s a great blend of algorithmic evolution, theoretical rigor, and practical
guidance. Whether you are a student, researcher, or industry
professional, this book will equip you with the use cases and solutions
needed to level-up your knowledge of generative AI. Well done!
—Chris Fregly, Principal Solution Architect, Generative
AI at AWS
In the heart of the GenAI revolution, this indispensable guide masterfully
balances theory and practice, navigating the vast landscape of large
language models to equip readers with the knowledge needed for
immediate and transformative impact in the field of AI.
—Tarun Narayanan Venkatachalam, AI Researcher,
University of Washington
Timely reading to get hands-on experience with language models.
—Emir Muñoz, Genesys
Hands-On Large Language Models brings clarity and practical examples
to cut through the hype of AI. It provides a wealth of great diagrams and
visual aids to supplement the clear explanations. The worked examples
and code make concrete what other books leave abstract. The book starts
with simple introductory beginnings, and steadily builds in scope. By the
final chapters, you will be fine-tuning and building your own large
language models with confidence.
—Leland McInnes, Researcher at the Tutte Institute for
Mathematics and Computing
Praise for Hands-On Large Language Models
This is an exceptional guide to the world of language models and their
practical applications in industry. Its highly-visual coverage of
generative, representational, and retrieval applications of language
models empowers readers to quickly understand, use, and refine LLMs.
Highly recommended!
—Nils Reimers, Director of Machine Learning at Cohere |
creator of sentence-transformers
Jay and Maarten have continued their tradition of providing beautifully
illustrated and insightful descriptions of complex topics in their new
book. Bolstered with working code, timelines, and references to key
papers, their book is a valuable resource for anyone looking to
understand the main techniques behind how Large Language Models are
built.
—Andrew Ng, founder of DeepLearning.AI
I can’t think of another book that is more important to read right now. On
every single page, I learned something that is critical to success in this
era of language models.
—Josh Starmer, StatQuest
If you’re looking to get up to speed in everything regarding LLMs, look
no further! In this wonderful book, Jay and Maarten will take you from
zero to expert in the history and latest advances in large language
models. With very intuitive explanations, great real-life examples, clear
illustrations, and comprehensive code labs, this book lifts the curtain on
the complexities of transformer models, tokenizers, semantic search,
RAG, and many other cutting-edge technologies. A must read for anyone
interested in the latest AI technology!
—Luis Serrano, PhD, Founder and CEO of Serrano
Academy
This book is a must-read for anyone interested in the rapidly-evolving
field of generative AI. With a focus on both text and visual embeddings,
it’s a great blend of algorithmic evolution, theoretical rigor, and practical
guidance. Whether you are a student, researcher, or industry
professional, this book will equip you with the use cases and solutions
needed to level-up your knowledge of generative AI. Well done!
—Chris Fregly, Principal Solution Architect, Generative
AI at AWS
In the heart of the GenAI revolution, this indispensable guide masterfully
balances theory and practice, navigating the vast landscape of large
language models to equip readers with the knowledge needed for
immediate and transformative impact in the field of AI.
—Tarun Narayanan Venkatachalam, AI Researcher,
University of Washington
Timely reading to get hands-on experience with language models.
—Emir Muñoz, Genesys
Hands-On Large Language Models brings clarity and practical examples
to cut through the hype of AI. It provides a wealth of great diagrams and
visual aids to supplement the clear explanations. The worked examples
and code make concrete what other books leave abstract. The book starts
with simple introductory beginnings, and steadily builds in scope. By the
final chapters, you will be fine-tuning and building your own large
language models with confidence.
—Leland McInnes, Researcher at the Tutte Institute for
Mathematics and Computing
Praise for Hands-On Large Language Models
This is an exceptional guide to the world of language models and their
practical applications in industry. Its highly-visual coverage of
generative, representational, and retrieval applications of language
models empowers readers to quickly understand, use, and refine LLMs.
Highly recommended!
—Nils Reimers, Director of Machine Learning at Cohere |
creator of sentence-transformers
Jay and Maarten have continued their tradition of providing beautifully
illustrated and insightful descriptions of complex topics in their new
book. Bolstered with working code, timelines, and references to key
papers, their book is a valuable resource for anyone looking to
understand the main techniques behind how Large Language Models are
built.
—Andrew Ng, founder of DeepLearning.AI
I can’t think of another book that is more important to read right now. On
every single page, I learned something that is critical to success in this
era of language models.
—Josh Starmer, StatQuest
If you’re looking to get up to speed in everything regarding LLMs, look
no further! In this wonderful book, Jay and Maarten will take you from
zero to expert in the history and latest advances in large language
models. With very intuitive explanations, great real-life examples, clear
illustrations, and comprehensive code labs, this book lifts the curtain on
the complexities of transformer models, tokenizers, semantic search,
RAG, and many other cutting-edge technologies. A must read for anyone
interested in the latest AI technology!
—Luis Serrano, PhD, Founder and CEO of Serrano
Academy
This book is a must-read for anyone interested in the rapidly-evolving
field of generative AI. With a focus on both text and visual embeddings,
it’s a great blend of algorithmic evolution, theoretical rigor, and practical
guidance. Whether you are a student, researcher, or industry
professional, this book will equip you with the use cases and solutions
needed to level-up your knowledge of generative AI. Well done!
—Chris Fregly, Principal Solution Architect, Generative
AI at AWS
In the heart of the GenAI revolution, this indispensable guide masterfully
balances theory and practice, navigating the vast landscape of large
language models to equip readers with the knowledge needed for
immediate and transformative impact in the field of AI.
—Tarun Narayanan Venkatachalam, AI Researcher,
University of Washington
Timely reading to get hands-on experience with language models.
—Emir Muñoz, Genesys
Hands-On Large Language Models brings clarity and practical examples
to cut through the hype of AI. It provides a wealth of great diagrams and
visual aids to supplement the clear explanations. The worked examples
and code make concrete what other books leave abstract. The book starts
with simple introductory beginnings, and steadily builds in scope. By the
final chapters, you will be fine-tuning and building your own large
language models with confidence.
—Leland McInnes, Researcher at the Tutte Institute for
Mathematics and Computing
Praise for Hands-On Large Language Models
This is an exceptional guide to the world of language models and their
practical applications in industry. Its highly-visual coverage of
generative, representational, and retrieval applications of language
models empowers readers to quickly understand, use, and refine LLMs.
Highly recommended!
—Nils Reimers, Director of Machine Learning at Cohere |
creator of sentence-transformers
Jay and Maarten have continued their tradition of providing beautifully
illustrated and insightful descriptions of complex topics in their new
book. Bolstered with working code, timelines, and references to key
papers, their book is a valuable resource for anyone looking to
understand the main techniques behind how Large Language Models are
built.
—Andrew Ng, founder of DeepLearning.AI
I can’t think of another book that is more important to read right now. On
every single page, I learned something that is critical to success in this
era of language models.
—Josh Starmer, StatQuest
If you’re looking to get up to speed in everything regarding LLMs, look
no further! In this wonderful book, Jay and Maarten will take you from
zero to expert in the history and latest advances in large language
models. With very intuitive explanations, great real-life examples, clear
illustrations, and comprehensive code labs, this book lifts the curtain on
the complexities of transformer models, tokenizers, semantic search,
RAG, and many other cutting-edge technologies. A must read for anyone
interested in the latest AI technology!
—Luis Serrano, PhD, Founder and CEO of Serrano
Academy
This book is a must-read for anyone interested in the rapidly-evolving
field of generative AI. With a focus on both text and visual embeddings,
it’s a great blend of algorithmic evolution, theoretical rigor, and practical
guidance. Whether you are a student, researcher, or industry
professional, this book will equip you with the use cases and solutions
needed to level-up your knowledge of generative AI. Well done!
—Chris Fregly, Principal Solution Architect, Generative
AI at AWS
In the heart of the GenAI revolution, this indispensable guide masterfully
balances theory and practice, navigating the vast landscape of large
language models to equip readers with the knowledge needed for
immediate and transformative impact in the field of AI.
—Tarun Narayanan Venkatachalam, AI Researcher,
University of Washington
Timely reading to get hands-on experience with language models.
—Emir Muñoz, Genesys
Hands-On Large Language Models brings clarity and practical examples
to cut through the hype of AI. It provides a wealth of great diagrams and
visual aids to supplement the clear explanations. The worked examples
and code make concrete what other books leave abstract. The book starts
with simple introductory beginnings, and steadily builds in scope. By the
final chapters, you will be fine-tuning and building your own large
language models with confidence.
—Leland McInnes, Researcher at the Tutte Institute for
Mathematics and Computing"""
        )

        responses = grpc_stub.Chat(request)

        result = ""

        for response in responses:
            result += response.reply

        end = time.time()

        latency = end - start

        return latency, True

    except Exception as e:
        return None, False


# ==========================================

# METRIC CALCULATOR

# ==========================================


def calculate_metrics(results, total_time):

    successful_latencies = [
        latency for latency, success in results if success and latency is not None
    ]

    success_count = len(successful_latencies)

    failure_count = len(results) - success_count

    success_rate = (success_count / len(results)) * 100

    error_rate = (failure_count / len(results)) * 100

    if success_count > 0:
        avg_duration = np.mean(successful_latencies)

        throughput = success_count / total_time

        p95_latency = np.percentile(successful_latencies, 95)

    else:
        avg_duration = 0

        throughput = 0

        p95_latency = 0

    return {
        "total_time": total_time,
        "avg_duration": avg_duration,
        "throughput": throughput,
        "p95_latency": p95_latency,
        "success_count": success_count,
        "failure_count": failure_count,
        "success_rate": success_rate,
        "error_rate": error_rate,
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
        rest_results = list(executor.map(rest_request, range(total_requests)))

    rest_total_time = time.time() - rest_start

    rest_metrics = calculate_metrics(rest_results, rest_total_time)

    # ======================================
    # gRPC BENCHMARK
    # ======================================

    grpc_start = time.time()

    with ThreadPoolExecutor(max_workers=workers) as executor:
        grpc_results = list(executor.map(grpc_request, range(total_requests)))

    grpc_total_time = time.time() - grpc_start

    grpc_metrics = calculate_metrics(grpc_results, grpc_total_time)

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
            "rest_success_rate": rest_metrics["success_rate"],
            "rest_error_rate": rest_metrics["error_rate"],
            "grpc_success_rate": grpc_metrics["success_rate"],
            "grpc_error_rate": grpc_metrics["error_rate"],
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
