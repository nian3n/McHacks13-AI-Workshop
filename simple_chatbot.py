#import necessary libraries
import openai #helps ur program read environment variables (eg. your API key)
import os #lets ur Python program talk to the OpenAI models


openai.api_key = os.getenv("OPENAI_API_KEY")

#define a function to chat with GPT
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[ {"role": "user", "content": prompt} ]
    )
    return response.choices[0].message['content'].strip()


if __name__ == "__main__":
    print("ChatBot: Hey! Feel free to chat with me. Type 'exit' to stop.\n")
    while True:
        user_input = input("You: ")

        if user_input in ["hi", "hello", "hey", "yo"]:
            print("ChatBot: Hey! How’s it going?\n")
            continue

        if "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M")
            print(f"ChatBot: It's around {now}.")
            continue

        if user_input.lower() in ["exit", "quit","bye"]:
            break
            
        reply = chat_with_gpt(user_input)
        print(f"ChatBot: {reply}")