#!/usr/bin/env python3
"""Example: Forex trading automation."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.ai_automation import AIAutomationCoordinator


def trading_automation_example():
    """Example of automated trading workflow."""
    print("=" * 70)
    print("TRADING AUTOMATION EXAMPLE")
    print("=" * 70)
    print("""
This example demonstrates how to use the AI automation system for trading:

1. Navigate to a trading platform
2. Log in
3. Check current forex prices
4. Analyze market conditions (with DeepSeek reasoning)
5. Place a trade order
6. Monitor position

NOTE: This is an example template. Adapt URLs and selectors to your platform.
      NEVER use this with real money without thorough testing!
    """)

    coordinator = AIAutomationCoordinator(headless=False)

    trading_goals = [
        "Navigate to the trading platform",
        "Log in to the account",
        "Find EUR/USD currency pair",
        "Analyze current price and recent movement",
        "Determine if conditions are favorable for trading",
        "If favorable, place a small buy order",
    ]

    for goal in trading_goals:
        print(f"\n{'='*70}")
        print(f"GOAL: {goal}")
        print('='*70)

        def on_step(info):
            status = "✓" if info['success'] else "✗"
            print(f"{status} Step {info['step']}: {info['observation'][:80]}")

        result = coordinator.step_by_step(
            goal=goal,
            initial_url="https://trading-example.com",
            on_step=on_step
        )

        if not result['success']:
            print(f"⚠ Goal failed at step {result['steps']}")
            break
        else:
            print(f"✓ Goal completed in {result['steps']} steps")

    print("\n" + "="*70)
    print("TRADING WORKFLOW COMPLETE")
    print("="*70)


def interactive_trading_session():
    """Interactive trading session with manual goals."""
    print("\nInteractive Trading Session")
    print("Enter your trading goals (one per line, empty line to finish):\n")

    coordinator = AIAutomationCoordinator(headless=False)

    while True:
        goal = input("Enter goal: ").strip()
        if not goal:
            break

        print(f"\nExecuting: {goal}")

        result = coordinator.step_by_step(
            goal=goal,
            initial_url="https://trading-example.com",
            on_step=lambda info: print(f"  Step {info['step']}: {info['observation']}")
        )

        print(f"\nResult: {'Success' if result['success'] else 'Failed'}")
        print(f"Steps taken: {result['steps']}\n")


if __name__ == "__main__":
    print("\nForex Trading Automation Examples\n")

    print("Available examples:")
    print("1. trading_automation_example() - Full workflow example")
    print("2. interactive_trading_session() - Manual goal entry\n")

    print("To get started:")
    print("- Set up DEEPSEEK_API_KEY environment variable")
    print("- Update the trading platform URL in the examples")
    print("- Adapt CSS selectors for your platform")
    print("- Test with small amounts before using with real money\n")

    try:
        trading_automation_example()
    except KeyboardInterrupt:
        print("\n\nAutomation stopped by user")
    except Exception as e:
        print(f"\nError: {e}")
        print("Make sure:")
        print("- DEEPSEEK_API_KEY is set")
        print("- Chrome/Chromium browser is installed")
        print("- Dependencies are installed (pip install -r requirements.txt)")
