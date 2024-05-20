import os
from dotenv import load_dotenv
from openai import OpenAI
from typing import List
from app.schemas.chatgpt import Message
from app.config.chatgpt import chatgpt_params

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def create_chat_completions(prompt: List[Message]) -> str:
    params = {"messages": prompt, **chatgpt_params}

    response = client.chat.completions.create(**params)

    return response.choices[0].message.content
