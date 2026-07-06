# Custom Agents Integration Guide

This guide details the procedure for introducing new agents and crews into the Nexsus Agent Swarms Orchestrator.

## 1. Defining Agent Configuration

Agents are configured via YAML templates within the `crews/` directory.

### Example Configuration:
```yaml
agents:
  system_monitor:
    role: "System Monitor"
    goal: "Verify system health and resource consumption"
    backstory: "An automated monitor agent designed to keep track of resource stats."
    verbose: true
    tools:
      - SystemDiagnosticsTool
```

## 2. Dynamic Tool Registration

Any subclass of `SwarmTool` defined in `backend/app/tools/` is scanned and registered automatically by `ToolRegistry`. No manual imports or configuration edits are required.
