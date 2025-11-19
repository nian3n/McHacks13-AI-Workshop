
from openai import OpenAI # Import the OpenAI package
import os # Import the os package

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "tell a good joke in the form of a question. Do not yet give the answer."}
  ]
)

print(completion.choices[0].message.content)
