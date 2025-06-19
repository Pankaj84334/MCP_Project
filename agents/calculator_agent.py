# Notice: we do NOT import FastAPI here!
from mcp.server.fastmcp import FastMCP

# We’ll import the singleton `mcp` instance from main later
# so here we just define a function that takes an MCP instance:
mcp=FastMCP("Math")
@mcp.tool()
def add(a: int, b: int) -> str:
    return f"Math Response: {a + b}"

@mcp.tool()
def subtract(a: int, b: int) -> str:
    return f"Math Response: {a - b}"

@mcp.tool()
def multiply(a: int, b: int) -> str:
    return f"Math Response: {a * b}"

@mcp.tool()
def divide(a: int, b: int) -> str:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return f"Math Response: {a / b}"
if __name__ == "__main__":
    mcp.run(
        transport="stdio"
    )