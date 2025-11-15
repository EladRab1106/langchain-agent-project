from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI


def calculate(expression: str):
    try:
        result = eval(expression)
        return result
    except Exception:
        return "Error: Invalid expression"


calculator_tool = Tool(
    name="calculator",
    description="returns the value of a mathematical expression",
    func=calculate,
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

agent = create_agent(llm, [calculator_tool])


def run_agent_request(user_input: str):
    state = agent.invoke({
        "messages": [
            HumanMessage(content=user_input),
        ]
    })

    messages = state["messages"]
    for msg in reversed(messages):
        content = getattr(msg, "content", None)
        if content:
            return content

    return "No response from agent"
