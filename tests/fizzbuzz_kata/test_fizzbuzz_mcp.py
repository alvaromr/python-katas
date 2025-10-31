from fastmcp import Client
from fastmcp.client import FastMCPTransport

from pythonkatas.fizzbuzz_kata.fizzbuzz_mcp import mcp

import pytest_asyncio
import pytest

@pytest_asyncio.fixture
async def main_mcp_client():
    async with Client(transport=mcp) as mcp_client:
        yield mcp_client

@pytest.mark.asyncio
async def test_list_tools(main_mcp_client: Client[FastMCPTransport]):
    list_tools = await main_mcp_client.list_tools()

    assert len(list_tools) == 2

@pytest.mark.asyncio
async def test_fizzbuzz_tool(main_mcp_client: Client[FastMCPTransport]):
    fb = await main_mcp_client.call_tool(
            "fizzbuzz",
            {"number": 15},
    )
    assert fb.data == "FizzBuzz"

@pytest.mark.asyncio
async def test_fizzbuzz_custom_rules(main_mcp_client: Client[FastMCPTransport]):
    fb = await main_mcp_client.call_tool(
        "fizzbuzz_custom_rules",
        {
            "number": 15,
            "rules": [
                {"divisor": 3, "word": "Banana"},
                {"divisor": 5, "word": "Apple"}
            ]
        },
    )
    assert fb.data == "BananaApple"