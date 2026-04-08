# AI Finance Agent

A conversational AI agent that lets users interact with a personal fintech API using natural language. Built with LangChain and powered by Groq, users can check their wallet balance and send money just by chatting.


## Tech Stack
- Agent Framework: LangChain
- LLM: Groq (llama-3.3-70b-versatile)
- Session storage: JSON file (.session.json)


## Setup
1. Clone repo
```
git clone https://github.com/your-username/ai-finance-agent.git
cd ai-finance-agent
```

2. Install dependencies
```
pip install fastapi uvicorn langchain langchain-core langchain-groq langchain-community python-dotenv requests
```

3. Set up environment variables
Create a .env file inside the agent/ folder:
```
GROQ_API_KEY=your_groq_api_key_here
```

4. Start the API
```
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

5. Run the agent
```
cd agent
python main.py
```
---

## Usage
- Login — Login with username <user> and password <pass>
- Check balance — What is my balance?
- Send money — Send <amount> to <username>
- Check transaction history — show my transaction history, show only sent transactions, show received transactions