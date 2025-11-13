import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[ {"role": "user", "content": prompt} ]
    )
    return response.choices[0].message['content'].strip()
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit","bye"]:
            break
            
        reply = chat_with_gpt(user_input)
        print(f"ChatBot: {reply}")