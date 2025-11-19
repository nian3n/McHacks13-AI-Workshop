import os
from openai import OpenAI

# Configuration variables
api_key = os.getenv("OPENAI_API_KEY") or os.getenv("TOGETHER_API_KEY")
client = OpenAI(api_key=api_key)
MODEL = "gpt-4o-mini"  
TEMPERATURE = 0.9
# ---- Config ----
MAX_TOKENS = 100

PERSONALITY = {
    "grumpy": (
        "You are a grumpy assistant who complains about answering questions, "
        "but still gives correct and helpful answers."
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


def chat(user_input: str):
    global messages

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    return reply


def set_personality(p: str):
    global CURR_P, messages

    p = p.strip().lower()
    if p not in PERSONALITY:
        return f"Unknown mood '{p}'. Available: {', '.join(PERSONALITY.keys())}"

    CURR_P = p
    messages = [{"role": "system", "content": build_system_prompt()}]

    return f"Personality switched to: {p}."


def forget():
    global messages
    messages = [{"role": "system", "content": build_system_prompt()}]
    return "Memory cleared."

# ---- Main Loop ----
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in {"exit", "quit"}:
            print("Assistant: Goodbye!")
            break
        if not user_input:
            continue  # ignore empty input

        if user_input.startswith("/"):
            parts = user_input.split(maxsplit=1)
            cmd = parts[0].lower()
            arg = parts[1] if len(parts) > 1 else ""

            if cmd == "/personality":
                if arg:
                    print("Assistant:", set_personality(arg), "\n")
                else:
                    print("Assistant: Choose a personality: grumpy, friendly, patient\n")
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
        print("Assistant:", answer, "\n")
