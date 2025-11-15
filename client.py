from agent import run_agent_request

while True:
    text = input("Enter expression: ")
    reply = run_agent_request(text)
    print("Result:", reply)
