import os
from ollama import Client

MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://kmhvy-34-125-197-209.run.pinggy-free.link")

client = Client(host=OLLAMA_HOST)

def summarize_note(content: str) -> str:
    prompt = f"Tóm tắt nội dung sau đây trong 1 câu ngắn gọn: {content}"
    messages = [{"role": "user", "content": prompt}]
    response = client.chat(model=MODEL, messages=messages)
    return response["message"]["content"]