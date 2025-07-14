# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

# Add an additional tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers
    """
    return a + b