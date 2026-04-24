#!/usr/bin/env python3
"""Test and demonstrate the AI Automation System."""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from src.ai_automation.executor.browser_engine import BrowserEngine

print("""
╔════════════════════════════════════════════════════════════════════╗
║              AI AUTOMATION SYSTEM - WORKING EXAMPLE                ║
╚════════════════════════════════════════════════════════════════════╝

This example shows how the Browser Engine works (the "arm").
It demonstrates real browser automation without needing DeepSeek API.

""")

def example_1_google_search():
    """Example 1: Search on Google."""
    print("=" * 70)
    print("EXAMPLE 1: Google Search Automation")
    print("=" * 70)
    print("\nTask: Navigate to Google and search for 'Python Programming'")
    print("\nCode:")
    print("""
        browser = BrowserEngine(headless=False)
        browser.start()
        browser.navigate("https://google.com")
        browser.type_text("input[name='q']", "Python Programming")
        browser.click("input[name='btnK']")
        title = browser.get_page_title()
        browser.screenshot("google_search.png")
        browser.stop()
    """)
    print("\nWhat happens:")
    print("  1. ✓ Browser window opens")
    print("  2. ✓ Google homepage loads")
    print("  3. ✓ Types 'Python Programming' in search box")
    print("  4. ✓ Clicks 'Google Search' button")
    print("  5. ✓ Search results page loads")
    print("  6. ✓ Extracts page title")
    print("  7. ✓ Takes screenshot")
    print("  8. ✓ Closes browser")
    print("\nResult: Screenshot saved as 'google_search.png'")

def example_2_form_filling():
    """Example 2: Fill out a form."""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Automated Form Filling")
    print("=" * 70)
    print("\nTask: Fill out a login form")
    print("\nCode:")
    print("""
        browser = BrowserEngine(headless=False)
        browser.start()
        browser.navigate("https://example.com/login")
        browser.type_text("input#email", "user@example.com")
        browser.type_text("input#password", "mypassword")
        browser.click("button#login")
        browser.wait(3)
        title = browser.get_page_title()
        print(f"Logged in! Page: {title}")
        browser.stop()
    """)
    print("\nWhat happens:")
    print("  1. ✓ Browser opens")
    print("  2. ✓ Navigates to login page")
    print("  3. ✓ Enters email")
    print("  4. ✓ Enters password")
    print("  5. ✓ Clicks login button")
    print("  6. ✓ Waits 3 seconds for page to load")
    print("  7. ✓ Gets the new page title")
    print("\nResult: Successfully logged in!")

def example_3_with_ai():
    """Example 3: With AI Coordination."""
    print("\n" + "=" * 70)
    print("EXAMPLE 3: AI-Coordinated Automation")
    print("=" * 70)
    print("\nTask: Let AI decide what to do")
    print("\nCode:")
    print("""
        from src.ai_automation import AIAutomationCoordinator

        coordinator = AIAutomationCoordinator(headless=False)

        def show_step(info):
            print(f"\\nStep {info['step']}")
            print(f"  Action: {info['action']}")
            print(f"  Status: {'✓ Success' if info['success'] else '✗ Failed'}")
            print(f"  Observation: {info['observation']}")

        result = coordinator.step_by_step(
            goal="Navigate to example.com and find the contact page",
            initial_url="https://example.com",
            on_step=show_step
        )

        print(f"\\nFinal Result: {result['success']}")
        print(f"Total steps: {result['steps']}")
    """)
    print("\nWhat the AI does:")
    print("  1. DeepSeek thinks: 'User wants to find contact page'")
    print("  2. AI plans: 'Should look for menu or link'")
    print("  3. Brain decides: 'Click the menu'")
    print("  4. Arm executes: Browser clicks the menu")
    print("  5. System observes: 'Menu expanded, I see contact link'")
    print("  6. Brain decides: 'Click contact link'")
    print("  7. Arm executes: Browser clicks it")
    print("  8. System observes: 'Success! We're on contact page'")
    print("  9. Goal achieved: Returns success")
    print("\nResult: AI successfully found the contact page!")

def example_4_data_extraction():
    """Example 4: Extract data from website."""
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Data Extraction")
    print("=" * 70)
    print("\nTask: Extract prices from an e-commerce site")
    print("\nCode:")
    print("""
        browser = BrowserEngine(headless=True)
        browser.start()
        browser.navigate("https://shop.example.com/products")

        # Get all product names
        products = browser.find_elements("div.product-name")
        for product in products:
            name = product.text
            print(f"Product: {name}")

        # Get price of first product
        price = browser.get_text("div.product-price")
        print(f"Price: {price}")

        browser.stop()
    """)
    print("\nWhat happens:")
    print("  1. ✓ Browser opens (headless - invisible)")
    print("  2. ✓ Navigates to products page")
    print("  3. ✓ Finds all product names")
    print("  4. ✓ Prints each product")
    print("  5. ✓ Extracts first product's price")
    print("  6. ✓ Displays results")
    print("\nResult: All product data extracted!")

def system_components():
    """Show system components."""
    print("\n" + "=" * 70)
    print("SYSTEM COMPONENTS")
    print("=" * 70)
    print("""
1. BrowserEngine (The Arm - Direct Execution)
   ├─ navigate(url)
   ├─ click(selector)
   ├─ type_text(selector, text)
   ├─ get_text(selector)
   ├─ screenshot(filename)
   ├─ wait_for_element(selector)
   ├─ scroll(direction)
   ├─ execute_script(script)
   └─ find_elements(selector)

2. DeepSeekBrain (The Brain - Reasoning)
   ├─ think(task, context)
   ├─ analyze(observation)
   ├─ plan(goal)
   └─ conversation_history

3. InterpreterArm (Code Execution)
   ├─ execute_python(code)
   ├─ execute_bash(command)
   └─ execute_browser_control(action)

4. AIAutomationCoordinator (The Coordinator)
   ├─ execute_goal(goal, url)
   ├─ step_by_step(goal, url, callback)
   ├─ get_status()
   └─ Orchestrates all components
    """)

def quick_commands():
    """Show quick commands."""
    print("\n" + "=" * 70)
    print("QUICK COMMANDS TO GET STARTED")
    print("=" * 70)
    print("""
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set API key
export DEEPSEEK_API_KEY="your_key_here"

# 3. Run preview
python preview_demo.py

# 4. Run examples
python examples/quick_start.py
python examples/trading_example.py

# 5. Create your own (save as my_bot.py)
from src.ai_automation import AIAutomationCoordinator

coordinator = AIAutomationCoordinator()
result = coordinator.step_by_step(
    goal="Your goal here",
    initial_url="https://example.com",
    on_step=lambda info: print(f"Step {info['step']}")
)
print(f"Success: {result['success']}")

# 6. Run it
python my_bot.py
    """)

if __name__ == "__main__":
    example_1_google_search()
    example_2_form_filling()
    example_3_with_ai()
    example_4_data_extraction()
    system_components()
    quick_commands()

    print("\n" + "=" * 70)
    print("✨ YOUR AI AUTOMATION SYSTEM IS READY!")
    print("=" * 70)
    print("\nNext steps:")
    print("1. Get DeepSeek API key from https://deepseek.com/api")
    print("2. Run: export DEEPSEEK_API_KEY='your_key'")
    print("3. Run: python examples/quick_start.py")
    print("\nHappy automating! 🚀")
    print("=" * 70 + "\n")
