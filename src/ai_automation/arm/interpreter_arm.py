"""Open Interpreter-based execution arm for browser control."""

import subprocess
import json
import tempfile
import os
from typing import Optional, Any
from pathlib import Path


class InterpreterArm:
    """Executes code to control the browser (Open Interpreter arm)."""

    def __init__(self):
        """Initialize interpreter arm."""
        self.last_error = None
        self.execution_history = []

    def execute_python(self, code: str) -> dict:
        """Execute Python code and return result.

        Args:
            code: Python code to execute

        Returns:
            Execution result with output and status
        """
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(code)
                temp_file = f.name

            try:
                result = subprocess.run(
                    ["python", temp_file],
                    capture_output=True,
                    text=True,
                    timeout=30
                )

                output = result.stdout
                error = result.stderr
                success = result.returncode == 0

                execution_record = {
                    "code": code,
                    "output": output,
                    "error": error,
                    "success": success
                }
                self.execution_history.append(execution_record)

                return {
                    "success": success,
                    "output": output,
                    "error": error,
                    "returncode": result.returncode
                }

            finally:
                os.unlink(temp_file)

        except subprocess.TimeoutExpired:
            self.last_error = "Code execution timeout (30s)"
            return {
                "success": False,
                "output": "",
                "error": "Execution timeout",
                "returncode": -1
            }
        except Exception as e:
            self.last_error = str(e)
            return {
                "success": False,
                "output": "",
                "error": str(e),
                "returncode": -1
            }

    def execute_browser_control(self, action: str, **kwargs) -> dict:
        """Execute browser control action.

        Args:
            action: Type of action (click, type, navigate, screenshot, etc.)
            **kwargs: Action-specific parameters

        Returns:
            Result of the action
        """
        code = self._generate_selenium_code(action, kwargs)
        return self.execute_python(code)

    def _generate_selenium_code(self, action: str, params: dict) -> str:
        """Generate Selenium code for browser action.

        Args:
            action: The action type
            params: Parameters for the action

        Returns:
            Python code to execute
        """
        setup = """from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
"""

        if action == "navigate":
            url = params.get("url", "")
            code = setup + f'driver.get("{url}")\ntime.sleep(2)'

        elif action == "click":
            selector = params.get("selector", "")
            code = setup + f'''element = driver.find_element(By.CSS_SELECTOR, "{selector}")
element.click()
time.sleep(1)'''

        elif action == "type":
            selector = params.get("selector", "")
            text = params.get("text", "")
            code = setup + f'''element = driver.find_element(By.CSS_SELECTOR, "{selector}")
element.send_keys("{text}")'''

        elif action == "screenshot":
            code = setup + 'driver.save_screenshot("screenshot.png")\nprint("Screenshot taken")'

        elif action == "get_text":
            selector = params.get("selector", "")
            code = setup + f'''element = driver.find_element(By.CSS_SELECTOR, "{selector}")
print(element.text)'''

        else:
            code = setup + 'print("Unknown action")'

        code += "\ndriver.quit()"
        return code

    def execute_bash(self, command: str) -> dict:
        """Execute bash command.

        Args:
            command: Bash command to run

        Returns:
            Execution result
        """
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )

            return {
                "success": result.returncode == 0,
                "output": result.stdout,
                "error": result.stderr,
                "returncode": result.returncode
            }

        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "output": "",
                "error": "Command timeout",
                "returncode": -1
            }
        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": str(e),
                "returncode": -1
            }

    def get_execution_history(self) -> list:
        """Get execution history."""
        return self.execution_history
