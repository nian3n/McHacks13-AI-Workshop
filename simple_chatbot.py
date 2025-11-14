#import necessary libraries
import os # helps your program read environment variables (e.g. your API key)
from openai import OpenAI # lets your Python program talk to the OpenAI models

# Load API key 
api_key = os.getenv("OPENAI_API_KEY") 

# Create a client
client = OpenAI(api_key=api_key)

# Send a request 
response = client.chat.completions.create(
    model="gpt-4o-mini",  
    messages=[
        {"role": "system", "content": "You are a grumpy assistant who hates answering questions."},
        {"role": "user", "content": "What is your take on pineapple pizzas?"}
    ],
    temperature=0.6,
    max_tokens=150
)

# Extract and display the reply
reply = response.choices[0].message.content
print("Assistant:", reply)