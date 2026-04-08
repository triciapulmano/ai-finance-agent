# AI Finance Agent

A conversational AI agent that lets users interact with a personal fintech API using natural language. Built with LangChain and powered by Groq, users can check their wallet balance and send money just by chatting.


## Tech Stack
- Agent Framework: LangChain
- LLM: Groq (llama-3.3-70b-versatile)
- Session storage: JSON file (.session.json)


## Setup
1. Clone repo
<br>`git clone https://github.com/your-username/ai-finance-agent.git
<br>cd ai-finance-agent`

2. Install dependencies
<br>`pip install fastapi uvicorn langchain langchain-core langchain-groq langchain-community python-dotenv requests`

3. Set up environment variables
<br>Create a .env file inside the agent/ folder:
<br>`GROQ_API_KEY=your_groq_api_key_here`

4. Start the API
<br>`cd backend
<br>uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

5. Run the agent
<br>`cd agent
<br>python main.py`
---

## Usage
- Login — Login with username <user> and password <pass>
- Check balance — What is my balance?
- Send money — Send <amount> to <username>