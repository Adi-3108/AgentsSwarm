import json
import pytest
from backend.app.tools.weather_tool import WeatherTool

@pytest.mark.asyncio
async def test_weather_tool():
    tool = WeatherTool()
    res = await tool._run("Boston")
    data = json.loads(res)
    assert data["location"] == "Boston"
    assert data["temperature_c"] == 22.5
    assert data["mocked"] is True
