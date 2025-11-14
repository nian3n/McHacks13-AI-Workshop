#import necessary libraries
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_message = {
    "role": "system",
    "content": "You are a helpful and friendly assistant."
}

# Conversation history
messages = [system_message]


def chat_with_gpt(prompt):
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7,     
        max_tokens=300 #could be any value up to 4096      
    )

    reply = response.choices[0].message.content.strip()

    messages.append({"role": "assistant", "content": reply})
    return reply


if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("ChatBot: Bye!")
            break

        reply = chat_with_gpt(user_input)
        print(f"ChatBot: {reply}")
