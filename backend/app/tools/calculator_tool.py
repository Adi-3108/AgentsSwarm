import os
import json
import re
from backend.app.tools.base import SwarmTool

class CalculatorTool(SwarmTool):
    name = "CalculatorTool"
    description = "Evaluates basic arithmetic expressions safely. Input: a mathematical string (e.g. '2 * 3 + 4'). Output: JSON with result."

    async def _run(self, input: str) -> str:
        expr = input.strip()
        if not expr:
            return json.dumps({"error": "Empty expression"})
            
        # Basic validation: only digits, spaces, and operators (+, -, *, /, (, ))
        if not re.match(r"^[0-9+\-*/().\s]+$", expr):
            return json.dumps({"error": "Invalid character in expression"})
            
        try:
            # Note: eval is safe here because we strict-validate the characters with regex
            res = eval(expr, {"__builtins__": None}, {})
            return json.dumps({"expression": expr, "result": float(res)})
        except Exception as e:
            return json.dumps({"expression": expr, "error": str(e)})
