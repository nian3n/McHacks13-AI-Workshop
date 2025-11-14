## Getting Started
1. Clone the repo
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
2. Install dependencies
From the root directory:
pip install openai python-dotenv
3. Set your OpenAI API key
Create a .env file in the project root:
OPENAI_API_KEY=your_api_key_here
⚠️ Never hard-code your API key directly inside Python files.
⚠️ Never commit .env to GitHub.
4. Run your first script
For example, to run the basic chatbot:
python chatbot-basic/chatbot.py

## Beginner’s Tutorial for the OpenAI API in Python  
Based on the work of Tilburg AI (March 11, 2024)  

### 🛠 Requirements  
- Python (version 3.8 or plus) 
- IDE or text editor 
- An OpenAI account and API key  

---

### 🔧 Setup Instructions  

#### 1. Create or log into your OpenAI account  
Visit the [OpenAI API documentation](https://platform.openai.com/docs) and log in or sign up to obtain your API key.

#### 2. Generate an API Key  
Within the OpenAI dashboard go to the “API keys” section, generate a new key, and copy it. Note: you won’t be able to see it again after you leave the page.

#### 3. Store Your API Key as an Environment Variable  
**macOS / Linux (bash/zsh):**  
```bash
nano ~/.zshrc        # or ~/.bash_profile depending on your shell
# add:
export OPENAI_API_KEY='your_api_key_here'
source ~/.zshrc
```

## 📚More Learning Resources (beginners)
OpenAI Quickstart Guide
https://platform.openai.com/docs/quickstart?utm_source=chatgpt.com
Best Practices for Prompt Engineering
https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api
OpenAI API Docs (Models, Parameters, Examples)
https://platform.openai.com/docs
CS50: Introduction to AI with Python
https://cs50.harvard.edu/ai/
Dataquest: Build an AI Chatbot with Python + OpenAI
https://www.dataquest.io/blog/build-an-ai-chatbot-with-python-and-the-openai-api/?utm_source=chatgpt.com
