from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import ToolMessage
load_dotenv()
import asyncio
import os
async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["agents/calculator_agent.py"],
                "transport": "stdio",
                "description": "Performs arithmetic operations like add, subtract, multiply, divide"
            },
            "general": {
                "command": "python",
                "args": ["agents/general_agent.py"],
                "transport": "stdio",
                "description": "Handles general queries that are not related to math or weather"
            },
            "weather": {
                "command": "python",
                "args": ["agents/weather_agent.py"],
                "transport": "stdio",
                "description": "Provides weather information and forecasts"
            }
        }
    )
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
    tools = await client.get_tools()
    groq = ChatGroq(model="qwen-qwq-32b", temperature=0.0)
    agent = create_react_agent(
        groq,tools=tools,
    )
    # SYSTEM_PROMPT = (
    #     "You are a strict tool‐calling assistant. "
    #     "Whenever you invoke a tool, you must return its output EXACTLY COPYING every character. "
    #     "DO NOT Show thinking process, JUST RETURN THE OUTPUT AS IT IS."
    # )
    query1="where is champawat?"
    query2="what will be the weather of champawat in next 3 days?"
    query3="what is the weather of champawat?"
    query4="what is the value of (3+5)*8"
    messages = [
        # {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": query1},
    ]
    response = await agent.ainvoke({"messages": messages})
    tool_messages = [m for m in response['messages'] if isinstance(m, ToolMessage)]
    print("Tool used:")
    for tool in tool_messages:
        print(tool.name)
    print('\n')
    print(response['messages'][-1].content)
asyncio.run(main())