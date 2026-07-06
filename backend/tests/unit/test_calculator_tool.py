import json
import pytest
from backend.app.tools.calculator_tool import CalculatorTool

@pytest.mark.asyncio
async def test_calculator_tool_success():
    tool = CalculatorTool()
    res = await tool._run("2 * (3.5 + 1.5)")
    data = json.loads(res)
    assert data["result"] == 10.0

@pytest.mark.asyncio
async def test_calculator_tool_invalid():
    tool = CalculatorTool()
    res = await tool._run("2 * __import__('os').system('ls')")
    data = json.loads(res)
    assert "error" in data
