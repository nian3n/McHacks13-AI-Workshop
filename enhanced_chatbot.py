import os
from openai import OpenAI

# Configuration variables
api_key = os.getenv("OPENAI_API_KEY") or os.getenv("TOGETHER_API_KEY")
client = OpenAI(api_key=api_key)
MODEL = "gpt-4o-mini"  
TEMPERATURE = 0.9
MAX_TOKENS = 100

#configure bot personality
PERSONALITY = {
    "grumpy": (
        "You are a grumpy assistant who complains about answering questions, but still gives correct and helpful answers."
    ),
    "friendly": (
        "You are a friendly assistant who explains things clearly and is always supportive."
    ),
    "patient": (
        "You are a patient tutor who explains concepts step-by-step in simple terms."
    ),
}

CURR_P = "grumpy"

def build_system_prompt():
    return PERSONALITY[CURR_P]


# Initialize conversation history with system prompt
messages = [{"role": "system", "content": build_system_prompt()}]

def chat(user_input):
    #Send a message to the bot and return the response
    messages.append({"role": "user", "content": user_input})

    # Get AI response using full conversation history
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )

    reply = response.choices[0].message.content

    # Add current response to conversation history
    messages.append({"role": "assistant", "content": reply})

    return reply

def forget():
    global messages
    messages = [{"role": "system", "content": build_system_prompt()}]
    return "Conversation memory cleared."

def set_personality(p: str) -> str:
    """Change the bot’s personality and reset memory."""
    global CURR_P, messages
    if p not in PERSONALITY:
        return f"Unknown mood '{p}'. Available: {', '.join(PERSONALITY.keys())}"
    CURR_P = p
    messages = [{"role": "system", "content": build_system_prompt()}]
    return f"Personality switched to: {p}."

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in {"exit", "quit"}:
        break
    if not user_input:
        continue  # ignore empty input

    if user_input.startswith("/"):
        parts = user_input.split(maxsplit=1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if cmd == "/personality":
            print("Assistant:", set_personality(arg) if arg else "Choose a personality: grumpy, friendly, patient")
            continue

        if cmd == "/forget":
            print("Assistant:", forget(), "\n")
            continue

        if cmd == "/exit":
            print("Assistant: Goodbye!")
            break

        print("Assistant: Unknown command. Try /personality, /forget, or /exit.\n")
        continue

    answer = chat(user_input)
    print("Assistant:", answer)