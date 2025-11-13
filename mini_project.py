import os
from openai import OpenAI

# 1. Create the client (make sure OPENAI_API_KEY is set in your env)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL_NAME = "gpt-4o-mini"


def brainstorm_ideas(topic):
    """
    Ask the model to generate hackathon project ideas
    based on the given topic.
    """
    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI assistant that helps students brainstorm "
                "creative but realistic hackathon project ideas. "
                "Keep ideas short, concrete, and beginner-friendly."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Give me 3–5 hackathon project ideas based on this topic:\n"
                f"'{topic}'.\n"
                "For each idea, include:\n"
                "- a short title\n"
                "- 1–2 line description\n"
            ),
        },
    ]

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.8,   
        max_tokens=400, 
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    print("💡 AI Brainstorm Buddy")
    print("Type a theme or problem (or 'exit' to quit).")
    print()

    while True:
        topic = input("Your theme: ").strip()

        if topic.lower() in ["exit", "quit", "bye"]:
            print("Bye, good luck at your hackathons! 🚀")
            break

        if not topic:
            print("Please type something, e.g. 'mental health', 'climate', 'education tech'.")
            continue

        print("\n🔍 Brainstorming ideas...\n")
        ideas = brainstorm_ideas(topic)
        print(ideas)
        print("\n" + "-" * 50 + "\n")
