from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

import json
import os

from tools import *

os.environ["LANGCHAIN_TRACING_V2"] = "false"
load_dotenv()

def login_tool(data):
    if isinstance(data, dict):
        return login(data['username'], data['password'])
    elif isinstance(data, str):
        try:
            parsed = json.loads(data.replace("'", '"'))
            return login(parsed['username'], parsed['password'])
        except:
            parts = data.split()
            return login(parts[0], parts[1])
        
def send_money_tool(data):
    if isinstance(data, dict):
        return send_money(data['amount'], data['receiver_username'])
    elif isinstance(data, str):
        try:
            parsed = json.loads(data.replace("'", '"'))
            return send_money(parsed['amount'], parsed['receiver_username'])
        except:
            return {"error": "Invalid input format for SendMoney"}
        
def transaction_history_tool(data):
    if isinstance(data, str):
        data = data.strip().lower()
        if "sent" in data:
            return get_transaction_history("sent")
        elif "received" in data:
            return get_transaction_history("received")
    return get_transaction_history()

tools = [
    Tool(
        name="Login",
        func=login_tool,
        description="Login a user. Input: {'username': str, 'password': str}"
    ),
    Tool(
        name="GetBalance",
        func=lambda _: get_balance(),
        description="Use this to check the user's wallet balance. The user is already logged in, call this directly without logging in first."
    ),
    Tool(
        name="SendMoney",
        func=send_money_tool,
        description="Use this to send money. The user is already logged in, call this directly without logging in first. Input should be dictionary: {'receiver_username': str, 'amount': float}"
    ),
    Tool(
        name="GetTransactionHistory",
        func=transaction_history_tool,
        description="Get the user's transaction history. Call this directly, no login needed. Optionally filter by type. Input: 'sent', 'received', or leave blank for all transactions."
    )
]

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

prompt = PromptTemplate.from_template("""You are a finance assistant. The user is ALREADY logged in. 
NEVER use the Login tool unless the user explicitly says "login" or "sign in".
For balance checks, use GetBalance directly.
For sending money, use SendMoney directly.

You have access to these tools:
{tools}

Use this format:
Question: the input question
Thought: your reasoning
Action: tool name (one of [{tool_names}])
Action Input: tool input
Observation: tool result
Thought: I now know the final answer
Final Answer: your response to the user

Begin:
Question: {input}
Thought: {agent_scratchpad}""")

agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True,
    max_iterations=3)