"""AI Automation system - DeepSeek brain + Open Interpreter arm for browser control."""

from .coordinator import AIAutomationCoordinator
from .brain.deepseek_brain import DeepSeekBrain
from .arm.interpreter_arm import InterpreterArm

__all__ = ["AIAutomationCoordinator", "DeepSeekBrain", "InterpreterArm"]
