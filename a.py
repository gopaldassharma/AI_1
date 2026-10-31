import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

groq_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = groq_client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are a funny travel guide."},
        {"role": "user",   "content": "tell me a joke about traveling to the moon."},
    ],
)
print("── Llama says:", response.choices[0].message.content) 