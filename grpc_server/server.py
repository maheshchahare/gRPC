from concurrent import futures
import time
import grpc

import multiply_pb2
import multiply_pb2_grpc


class ChatBotService(multiply_pb2_grpc.ChatBotServicer):
    def Chat(self, request, context):

        user_message = request.message

        if user_message.lower() == "hi":
            responses = ["Hello", "How", "can", "I", "help", "you?"]

        else:
            responses = ["I", "did", "not", "understand."]

        for text in responses:
            yield multiply_pb2.ChatResponse(reply=text)


def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    multiply_pb2_grpc.add_ChatBotServicer_to_server(ChatBotService(), server)

    server.add_insecure_port("[::]:50051")

    server.start()

    print("Chatbot gRPC server running on 50051")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()
