import grpc

import multiply_pb2
import multiply_pb2_grpc


def run():

    channel = grpc.insecure_channel("localhost:50051")

    stub = multiply_pb2_grpc.ChatBotStub(channel)

    user_input = input("You: ")

    request = multiply_pb2.ChatRequest(message=user_input)

    responses = stub.Chat(request)

    print("\nBot:", end="")

    for response in responses:
        print(response.reply, end=" ", flush=True)
    print("\n")


if __name__ == "__main__":
    run()
