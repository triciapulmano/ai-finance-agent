from langchain.agents import create_agent
from langchain_core.tools import Tool

from tools import login, get_balance, send_money
from langchain_ollama import ChatOllama


tools = [
    Tool(
        name="Login",
        func=lambda data: login(data['username'], data['password']),
        description="Login a user. Input: {'username': str, 'password': str}"
    ),
    Tool(
        name="Get Balance",
        func=lambda _: get_balance(),
        description="Use this to check the user's wallet balance"
    ),
    Tool(
        name="Send Money",
        func=lambda input: send_money(input['amount'], input['recipient']),
        description="Use this to send money. Input should be dictionary: {'receiver_username': str, 'amount': float}"
    )
]

llm = ChatOllama(
    model="llama2",
    temperature=0
)

agent = create_agent(
    tools=tools,
    model=llm
)