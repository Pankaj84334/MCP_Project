from mcp.server.fastmcp import FastMCP
import calculator_agent, weather_agent, general_agent

mcp = FastMCP("UnifiedMCP")

# register tools from each module
calculator_agent.register_tools(mcp)
weather_agent.register_tools(mcp)
general_agent.register_tools(mcp)

if __name__=="__main__":
    mcp.run(transport="streamable-http")  # single HTTP server on port 8000
