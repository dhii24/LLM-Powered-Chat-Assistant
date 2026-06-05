from groq import Groq
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

messages = []

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    reply = response.choices[0].message.content

    print("\nAI:", reply)

    messages.append({
        "role": "assistant",
        "content": reply
    })