import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

MODEL = "gpt-4o-mini"

messages = [
    {"role": "system", "content": "You are a helpful assistant who summarize files and answer questions simply but concisely."}
]

def chat(prompt):
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    reply = response.choices[0].message.content.strip()
    messages.append({"role": "assistant", "content": reply})
    return reply


def summarize_file(path):
    if not os.path.exists(path):
        return f"File not found: {path}"

    try:
        with open(path, "r") as f:
            content = f.read()
    except:
        return "Unable to read file. Try a different file."

    if len(content) > 6000:   # safety
        content = content[:6000] + "\n...[truncated]"

    prompt = "Summarize this file in 3–5 bullet points:\n\n" + content
    return chat(prompt)


print("Assistant: Type /file <path> to summarize a file, or /exit to quit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.startswith("/file"):
        path = user_input[5:].strip()
        print("Assistant:", summarize_file(path), "\n")
        continue

    if user_input.lower() in {"/exit", "exit", "quit"}:
        print("Assistant: Goodbye!")
        break

    print("Assistant:", chat(user_input), "\n")
