from openai import OpenAI
import os
from dotenv import load_dotenv
from prompts import get_system_prompt

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(messages):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content


def build_messages(chat_history):
    system_prompt = get_system_prompt()

    messages = [{"role": "system", "content": system_prompt}]

    for msg in chat_history:
        messages.append(msg)

    return messages
