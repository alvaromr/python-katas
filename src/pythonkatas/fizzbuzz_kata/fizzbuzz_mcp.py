from typing import List
from fastmcp import FastMCP, Context

from pythonkatas.fizzbuzz_kata.fizzbuzz import fizzbuzz, Rule

import logging

from fastmcp.utilities.logging import get_logger

to_client_logger = get_logger(name="fastmcp.server.context.to_client")
to_client_logger.setLevel(level=logging.DEBUG)
to_server_logger = get_logger(name="")

mcp = FastMCP(
    name="Fizzbuzz Server",
    instructions="""
        This is a Fizzbuzz server, which can fizzbuzz numbers.
        Fizzbuzzing a number means modifying the number with some words
        according to some rules.
    """,
)

@mcp.tool(
    description="Fizzbuzz a number with default rules",
    name="fizzbuzz",
)
async def fizzbuzz_default_rules(number: int, ctx: Context) -> str:
    fb = fizzbuzz(number)
    await ctx.debug(f"Fizzbuzzed {number} to {fb}")
    return fb

@mcp.tool(
    description="Fizzbuzz a number with custom rules",
)
async def fizzbuzz_custom_rules(number: int, rules: List[Rule], ctx: Context) -> str:
    fb = fizzbuzz(number, rules)
    await ctx.debug(f"Fizzbuzzed {number} to {fb} (Custom rules)")
    return fb

if __name__ == "__main__":
    port = 6278
    to_server_logger.info(
        f"""Add this mcp server with this config:
        
    "fizzbuzz-mcp": {{
      "type": "http",
      "url": "http://localhost:{port}/mcp"
    }}
        """
    )
    mcp.run(transport="http", host="127.0.0.1", port=port, show_banner=False)
