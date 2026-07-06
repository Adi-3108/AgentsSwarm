import os
import json
import pytest
from backend.app.tools.system_diagnostics_tool import SystemDiagnosticsTool

@pytest.mark.asyncio
async def test_system_diagnostics_mock(monkeypatch):
    monkeypatch.setenv("MOCK_TOOLS", "true")
    tool = SystemDiagnosticsTool()
    res = await tool._run(".")
    data = json.loads(res)
    assert data["status"] == "Healthy"
    assert "disk_total_gb" in data

@pytest.mark.asyncio
async def test_system_diagnostics_real(monkeypatch):
    monkeypatch.setenv("MOCK_TOOLS", "false")
    tool = SystemDiagnosticsTool()
    res = await tool._run(".")
    data = json.loads(res)
    assert "disk_total_gb" in data or "error" in data
