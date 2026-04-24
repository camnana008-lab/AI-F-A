"""Coordinator - connects DeepSeek brain + Open Interpreter arm."""

import json
import time
from typing import Optional, Callable, Any
from .brain.deepseek_brain import DeepSeekBrain
from .arm.interpreter_arm import InterpreterArm
from .executor.browser_engine import BrowserEngine


class AIAutomationCoordinator:
    """Coordinates DeepSeek (brain) + Open Interpreter (arm) for browser automation."""

    def __init__(self, deepseek_api_key: Optional[str] = None, headless: bool = False):
        """Initialize coordinator.

        Args:
            deepseek_api_key: DeepSeek API key
            headless: Run browser in headless mode
        """
        self.brain = DeepSeekBrain(api_key=deepseek_api_key)
        self.arm = InterpreterArm()
        self.browser = BrowserEngine(headless=headless)
        self.goal = None
        self.step = 0
        self.max_steps = 20
        self.observations = []

    def execute_goal(self, goal: str, initial_url: Optional[str] = None) -> dict:
        """Execute a goal using the brain-arm coordination.

        Args:
            goal: The goal to achieve
            initial_url: Initial URL to navigate to

        Returns:
            Execution result
        """
        self.goal = goal
        self.step = 0
        self.observations = []

        if not self.browser.start():
            return {"success": False, "error": "Failed to start browser"}

        try:
            if initial_url:
                self.browser.navigate(initial_url)
                time.sleep(2)

            while self.step < self.max_steps:
                self.step += 1

                context = self._build_context()
                action = self.brain.think(self.goal, context)

                success = self._execute_action(action)

                if not success:
                    break

                observation = self._observe_state()
                self.observations.append(observation)

                if self._is_goal_achieved():
                    return {
                        "success": True,
                        "goal": self.goal,
                        "steps": self.step,
                        "observations": self.observations
                    }

            return {
                "success": False,
                "goal": self.goal,
                "steps": self.step,
                "reason": "Max steps exceeded",
                "observations": self.observations
            }

        finally:
            self.browser.stop()

    def step_by_step(self, goal: str, initial_url: Optional[str] = None,
                     on_step: Optional[Callable] = None) -> dict:
        """Execute goal with callback for each step.

        Args:
            goal: The goal to achieve
            initial_url: Initial URL to navigate to
            on_step: Callback function called after each step

        Returns:
            Execution result
        """
        self.goal = goal
        self.step = 0
        self.observations = []

        if not self.browser.start():
            return {"success": False, "error": "Failed to start browser"}

        try:
            if initial_url:
                self.browser.navigate(initial_url)
                time.sleep(2)

            while self.step < self.max_steps:
                self.step += 1

                context = self._build_context()
                action = self.brain.think(self.goal, context)

                success = self._execute_action(action)

                observation = self._observe_state()
                self.observations.append(observation)

                if on_step:
                    on_step({
                        "step": self.step,
                        "action": action,
                        "observation": observation,
                        "success": success
                    })

                if not success:
                    break

                if self._is_goal_achieved():
                    return {
                        "success": True,
                        "goal": self.goal,
                        "steps": self.step,
                        "observations": self.observations
                    }

            return {
                "success": False,
                "goal": self.goal,
                "steps": self.step,
                "observations": self.observations
            }

        finally:
            self.browser.stop()

    def _build_context(self) -> str:
        """Build context string from current state.

        Returns:
            Context description
        """
        url = self.browser.get_page_url()
        title = self.browser.get_page_title()
        context = f"Current URL: {url}\nPage Title: {title}"

        if self.observations:
            context += f"\n\nLast observation: {self.observations[-1]}"

        return context

    def _execute_action(self, action: str) -> bool:
        """Execute an action suggested by the brain.

        Args:
            action: Action description/code

        Returns:
            True if execution succeeded
        """
        try:
            if action.startswith("click:"):
                selector = action.replace("click:", "").strip()
                return self.browser.click(selector)

            elif action.startswith("type:"):
                parts = action.replace("type:", "").strip().split("|", 1)
                if len(parts) == 2:
                    selector, text = parts
                    return self.browser.type_text(selector, text)

            elif action.startswith("navigate:"):
                url = action.replace("navigate:", "").strip()
                return self.browser.navigate(url)

            elif action.startswith("screenshot"):
                return self.browser.screenshot()

            elif action.startswith("scroll:"):
                direction = action.replace("scroll:", "").strip()
                self.browser.scroll(direction)
                return True

            elif action.startswith("wait:"):
                seconds = int(action.replace("wait:", "").strip())
                self.browser.wait(seconds)
                return True

            elif action.startswith("python:"):
                code = action.replace("python:", "").strip()
                result = self.arm.execute_python(code)
                return result["success"]

            else:
                return True

        except Exception as e:
            print(f"Action execution failed: {e}")
            return False

    def _observe_state(self) -> str:
        """Observe the current state of the page.

        Returns:
            Observation description
        """
        title = self.browser.get_page_title()
        url = self.browser.get_page_url()
        return f"Page: {title} | URL: {url}"

    def _is_goal_achieved(self) -> bool:
        """Check if goal has been achieved.

        Returns:
            True if goal is achieved
        """
        if not self.goal:
            return False

        source = self.browser.get_page_source()
        if not source:
            return False

        goal_lower = self.goal.lower()

        if "success" in goal_lower and "success" in source.lower():
            return True
        if "complete" in goal_lower and "complete" in source.lower():
            return True
        if "finish" in goal_lower and "finish" in source.lower():
            return True

        return False

    def get_status(self) -> dict:
        """Get current execution status.

        Returns:
            Status information
        """
        return {
            "goal": self.goal,
            "step": self.step,
            "max_steps": self.max_steps,
            "observations_count": len(self.observations),
            "url": self.browser.get_page_url()
        }
