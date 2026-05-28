from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

import time


app = FastAPI()


class ChatRequest(BaseModel):
    message: str


def generate_response(user_message):

    if user_message.lower() == "hi":
        responses = ["Hello ", "How ", "can ", "I ", "help ", "you?"]

    else:
        responses = ["I ", "did ", "not ", "understand."]

    for text in responses:
        yield text


@app.post("/chat")
def chat(request: ChatRequest):

    return StreamingResponse(
        generate_response(request.message), media_type="text/plain"
    )
