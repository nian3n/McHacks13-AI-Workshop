# from openai import OpenAI
# import os
# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# response = client.chat.completions.create(
#     model="gpt-4o-mini",          
#     messages=[                    
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Explain black holes simply."}
#     ],
#     temperature=0.7,              
#     max_tokens=150,               
#     stream=False                  
# )

# print(response.choices[0].message.content)


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
