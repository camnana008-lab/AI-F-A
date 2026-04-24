#!/usr/bin/env python3
"""Example: Browser game automation using AI brain + arm."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.ai_automation import AIAutomationCoordinator


def example_simple_navigation():
    """Example: Simple website navigation."""
    coordinator = AIAutomationCoordinator(headless=False)

    def on_step(step_info):
        print(f"\n--- Step {step_info['step']} ---")
        print(f"Action: {step_info['action'][:100]}")
        print(f"Observation: {step_info['observation']}")

    result = coordinator.step_by_step(
        goal="Find and click the 'Play' button on the game website",
        initial_url="https://example.com",
        on_step=on_step
    )

    print(f"\n=== RESULT ===")
    print(f"Success: {result['success']}")
    print(f"Steps taken: {result['steps']}")


def example_trading_site():
    """Example: Automated trading site interaction."""
    coordinator = AIAutomationCoordinator(headless=False)

    def on_step(step_info):
        print(f"\nStep {step_info['step']}: {step_info['observation']}")

    result = coordinator.step_by_step(
        goal="Log in to the trading platform and place a buy order",
        initial_url="https://trading-example.com",
        on_step=on_step
    )

    return result


def example_data_extraction():
    """Example: Extract data from a webpage."""
    coordinator = AIAutomationCoordinator(headless=False)

    if coordinator.browser.start():
        try:
            coordinator.browser.navigate("https://example.com")

            text = coordinator.browser.get_text("body")
            print(f"Page text: {text[:200]}")

            title = coordinator.browser.get_page_title()
            print(f"Page title: {title}")

            coordinator.browser.screenshot("example_screenshot.png")
            print("Screenshot saved")

        finally:
            coordinator.browser.stop()


if __name__ == "__main__":
    print("AI Automation System - Examples\n")
    print("This demonstrates the coordinator between:")
    print("- DeepSeek Brain (reasoning)")
    print("- Open Interpreter Arm (code execution)")
    print("- Browser Engine (Selenium-based automation)\n")

    print("To use these examples:")
    print("1. Set DEEPSEEK_API_KEY environment variable")
    print("2. Install dependencies: pip install -r requirements.txt")
    print("3. Update the URLs in examples to real websites\n")

    print("Available examples:")
    print("- example_simple_navigation(): Navigate and interact with a webpage")
    print("- example_trading_site(): Example for trading platform")
    print("- example_data_extraction(): Extract data from a webpage\n")
