from pydantic import BaseModel
from typing import List


class Content(BaseModel):
    type: str
    text: str


class Message(BaseModel):
    role: str
    content: List[Content]


class ChatRequest(BaseModel):
    prompt: List[Message]


class ChatResponse(BaseModel):
    response: str
