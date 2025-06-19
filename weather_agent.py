from mcp.server.fastmcp import FastMCP

# We’ll import the singleton `mcp` instance from main later
# so here we just define a function that takes an MCP instance:
mcp=FastMCP("Weather")

@mcp.tool()
def get_weather(city: str) -> str:
    return f"Weather Response: Sunny and 25°C in {city}"
@mcp.tool()
def get_forecast(city: str, days: int) -> str:
    return f"Weather Forecast: {city} for the next {days} days: Sunny with occasional clouds."

if __name__ == "__main__":
    mcp.run(
        transport="stdio"
    )