"""
Minimal FastMCP server example.
Exposes tools for use with Claude Code, GitHub Copilot, or Claude Desktop.
"""
import random
from fastmcp import FastMCP

mcp = FastMCP(name="Demo Server")


@mcp.tool
def roll_dice(n_dice: int = 1) -> list[int]:
    """Roll n_dice 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]


@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@mcp.tool
def reverse_string(text: str) -> str:
    """Reverse a string."""
    return text[::-1]


if __name__ == "__main__":
    # Run with stdio transport (default, used by Claude Code / Desktop)
    mcp.run()