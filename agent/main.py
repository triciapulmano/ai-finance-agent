from agent import agent

print("💰 Finance AI Agent running...")
print("Type 'exit' to quit.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    try:
        result = agent.invoke({"input": user_input})
        print("Agent:", result["output"])
    except Exception as e:
        print("Error:", e)