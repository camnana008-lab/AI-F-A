"""DeepSeek-based reasoning brain for AI automation."""

import json
import os
from typing import Optional, Any
import requests


class DeepSeekBrain:
    """Uses DeepSeek API for reasoning and decision making."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize DeepSeek brain.

        Args:
            api_key: DeepSeek API key (defaults to DEEPSEEK_API_KEY env var)
        """
        self.api_key = api_key or os.getenv("DEEPSEEK_API_KEY")
        if not self.api_key:
            raise ValueError("DEEPSEEK_API_KEY not provided or found in environment")

        self.base_url = "https://api.deepseek.com/v1"
        self.model = "deepseek-chat"
        self.conversation_history = []

    def think(self, task: str, context: Optional[str] = None) -> str:
        """Use DeepSeek to reason about a task.

        Args:
            task: The task to reason about
            context: Additional context about current state

        Returns:
            Reasoning and recommended action
        """
        prompt = f"Task: {task}"
        if context:
            prompt += f"\n\nCurrent Context:\n{context}"

        prompt += "\n\nProvide a clear, concise action plan with specific steps."

        return self._call_deepseek(prompt)

    def analyze(self, observation: str) -> dict:
        """Analyze an observation and extract key information.

        Args:
            observation: What was observed

        Returns:
            Analysis result as dictionary
        """
        prompt = f"""Analyze this observation and provide structured output:

Observation: {observation}

Provide JSON response with:
- analysis: Brief analysis of what's happening
- next_action: What should be done next
- confidence: Confidence level (0-1)
- risks: Any identified risks"""

        response = self._call_deepseek(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"analysis": response, "next_action": None, "confidence": 0.5}

    def plan(self, goal: str) -> list[dict]:
        """Create a step-by-step plan to achieve a goal.

        Args:
            goal: The goal to achieve

        Returns:
            List of steps to execute
        """
        prompt = f"""Create a detailed action plan to achieve this goal:

Goal: {goal}

Provide JSON array of steps with this format:
[
  {{"step": 1, "action": "...", "description": "..."}},
  ...
]"""

        response = self._call_deepseek(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return [{"step": 1, "action": "analyze", "description": response}]

    def _call_deepseek(self, prompt: str) -> str:
        """Call DeepSeek API.

        Args:
            prompt: The prompt to send

        Returns:
            Model's response
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        messages = self.conversation_history + [{"role": "user", "content": prompt}]

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 2000
        }

        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()

            data = response.json()
            content = data["choices"][0]["message"]["content"]

            self.conversation_history.append({"role": "user", "content": prompt})
            self.conversation_history.append({"role": "assistant", "content": content})

            if len(self.conversation_history) > 20:
                self.conversation_history = self.conversation_history[-20:]

            return content

        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"DeepSeek API error: {str(e)}")

    def reset_conversation(self):
        """Reset conversation history."""
        self.conversation_history = []
