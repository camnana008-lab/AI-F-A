#!/usr/bin/env python3
"""Quick start guide for AI Automation System."""

import sys
import os
import time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.ai_automation.coordinator import AIAutomationCoordinator
from src.ai_automation.executor.browser_engine import BrowserEngine


def demo_browser_automation():
    """Demonstrate browser automation without AI (using direct commands)."""
    print("=" * 60)
    print("DEMO 1: Direct Browser Automation")
    print("=" * 60)

    browser = BrowserEngine(headless=False)
    if browser.start():
        try:
            print("✓ Browser started")

            browser.navigate("https://google.com")
            print("✓ Navigated to Google")
            time.sleep(2)

            browser.type_text("input[name='q']", "Python Selenium")
            print("✓ Typed search query")
            time.sleep(1)

            browser.click("input[name='btnK']")
            print("✓ Clicked search button")
            time.sleep(3)

            title = browser.get_page_title()
            print(f"✓ Page title: {title}")

            browser.screenshot("google_search.png")
            print("✓ Screenshot saved as google_search.png")

        finally:
            browser.stop()
            print("✓ Browser closed\n")


def demo_ai_coordination():
    """Demonstrate AI-coordinated automation."""
    print("=" * 60)
    print("DEMO 2: AI-Coordinated Browser Automation")
    print("=" * 60)

    try:
        coordinator = AIAutomationCoordinator(headless=False)
        print("✓ Coordinator initialized")

        def log_step(step_info):
            print(f"\nStep {step_info['step']}:")
            print(f"  Action: {step_info['action'][:80]}")
            print(f"  Status: {'✓' if step_info['success'] else '✗'}")

        result = coordinator.step_by_step(
            goal="Navigate to Google and search for 'AI trading'",
            initial_url="https://google.com",
            on_step=log_step
        )

        print(f"\n{'='*60}")
        print(f"Result: {result['success']}")
        print(f"Total steps: {result['steps']}")

    except Exception as e:
        print(f"Note: AI demo requires DEEPSEEK_API_KEY set in environment")
        print(f"Error: {e}")


def setup_guide():
    """Print setup instructions."""
    print("=" * 60)
    print("SETUP INSTRUCTIONS")
    print("=" * 60)
    print("""
1. Install dependencies:
   pip install -r requirements.txt

2. Set up environment variables:
   export DEEPSEEK_API_KEY="your_key_here"

3. Get API keys:
   - DeepSeek: https://deepseek.com/api
   - You might need to adjust URLs for your specific use case

4. Run examples:
   python examples/quick_start.py
   python examples/example_game_automation.py

5. Create your own automation script:
   See examples/ for template patterns

Components:
  - DeepSeekBrain: Reasoning and decision making
  - InterpreterArm: Code execution
  - BrowserEngine: Selenium-based browser control
  - AIAutomationCoordinator: Orchestrates brain + arm
    """)


if __name__ == "__main__":
    setup_guide()
    print("\n")
    demo_browser_automation()
    print("\n")
    demo_ai_coordination()
