#!/usr/bin/env python3
"""Simple browser automation demo - works without API key."""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from src.ai_automation.executor.browser_engine import BrowserEngine
import time

print("""
╔══════════════════════════════════════════════════════════════════╗
║     SIMPLE BROWSER AUTOMATION DEMO (No API Key Needed!)          ║
╚══════════════════════════════════════════════════════════════════╝
""")

def demo_google_search():
    """Demo: Search on Google."""
    print("\n📌 DEMO: Google Search")
    print("=" * 60)
    print("Task: Open Google and search for 'Python automation'")
    print()

    browser = BrowserEngine(headless=False)

    if not browser.start():
        print("❌ Failed to start browser")
        return

    print("✓ Browser started")

    if browser.navigate("https://google.com"):
        print("✓ Navigated to Google")
        time.sleep(2)
    else:
        print("❌ Failed to navigate")
        browser.stop()
        return

    print(f"  Page title: {browser.get_page_title()}")

    if browser.type_text("input[name='q']", "Python automation"):
        print("✓ Typed search query")
    else:
        print("❌ Failed to type")
        browser.stop()
        return

    time.sleep(1)

    if browser.click("input[name='btnK']"):
        print("✓ Clicked search button")
        time.sleep(3)
    else:
        print("❌ Failed to click")
        browser.stop()
        return

    title = browser.get_page_title()
    print(f"✓ Search completed!")
    print(f"  Result page title: {title}")

    if browser.screenshot("demo_screenshot.png"):
        print("✓ Screenshot saved as demo_screenshot.png")

    browser.stop()
    print("✓ Browser closed\n")


def demo_github_explore():
    """Demo: Explore GitHub."""
    print("\n📌 DEMO: Explore GitHub")
    print("=" * 60)
    print("Task: Visit GitHub and explore trending repositories")
    print()

    browser = BrowserEngine(headless=False)

    if not browser.start():
        print("❌ Failed to start browser")
        return

    print("✓ Browser started")

    if browser.navigate("https://github.com"):
        print("✓ Navigated to GitHub")
        time.sleep(2)
    else:
        print("❌ Failed to navigate")
        browser.stop()
        return

    title = browser.get_page_title()
    print(f"✓ Page loaded: {title}")

    browser.scroll("down", 500)
    print("✓ Scrolled down")
    time.sleep(1)

    browser.screenshot("github_screenshot.png")
    print("✓ Screenshot saved")

    browser.stop()
    print("✓ Browser closed\n")


def demo_website_info():
    """Demo: Get website information."""
    print("\n📌 DEMO: Extract Website Information")
    print("=" * 60)
    print("Task: Visit example.com and extract information")
    print()

    browser = BrowserEngine(headless=False)

    if not browser.start():
        print("❌ Failed to start browser")
        return

    print("✓ Browser started")

    if browser.navigate("https://example.com"):
        print("✓ Navigated to example.com")
        time.sleep(2)
    else:
        print("❌ Failed to navigate")
        browser.stop()
        return

    title = browser.get_page_title()
    url = browser.get_page_url()

    print(f"✓ Information extracted:")
    print(f"  Title: {title}")
    print(f"  URL: {url}")

    h1_text = browser.get_text("h1")
    if h1_text:
        print(f"  Main heading: {h1_text}")

    browser.stop()
    print("✓ Browser closed\n")


def show_capabilities():
    """Show what the BrowserEngine can do."""
    print("\n📌 BROWSER ENGINE CAPABILITIES")
    print("=" * 60)
    print("""
Browser Control Methods:
├─ navigate(url)              → Go to a website
├─ click(selector)            → Click an element
├─ type_text(selector, text)  → Type text into a field
├─ get_text(selector)         → Get text from element
├─ screenshot(filename)       → Take a screenshot
├─ wait_for_element(selector) → Wait for element to load
├─ find_elements(selector)    → Find multiple elements
├─ scroll(direction, amount)  → Scroll the page
├─ get_page_title()          → Get page title
├─ get_page_url()            → Get current URL
├─ execute_script(script)     → Run JavaScript
└─ wait(seconds)              → Wait/pause

Selector Types Supported:
├─ CSS Selectors:     "button.primary"
├─ ID:                "#my-button"
├─ Class:             ".my-class"
├─ XPATH:             "//button[@id='my-button']"
└─ And more...
    """)


def show_quick_reference():
    """Quick reference guide."""
    print("\n📚 QUICK REFERENCE")
    print("=" * 60)
    print("""
Basic Automation Code:
───────────────────────

from src.ai_automation.executor.browser_engine import BrowserEngine

# Create browser
browser = BrowserEngine(headless=False)
browser.start()

# Navigation
browser.navigate("https://example.com")

# Form interaction
browser.type_text("input#email", "email@example.com")
browser.click("button#submit")

# Wait for page to load
browser.wait(2)

# Extract data
title = browser.get_page_title()
text = browser.get_text("h1")

# Take screenshot
browser.screenshot("result.png")

# Close browser
browser.stop()


Example Selectors:
─────────────────

# Find by CSS class
browser.click(".btn-primary")

# Find by ID
browser.type_text("#username", "user123")

# Find by attribute
browser.click("[data-test='submit']")

# Find by tag and class
browser.click("button.login-btn")

# Find by XPATH
browser.click("//button[contains(text(), 'Login')]")
    """)


if __name__ == "__main__":
    try:
        show_capabilities()
        show_quick_reference()

        print("\n" + "=" * 60)
        print("SELECT DEMO TO RUN:")
        print("=" * 60)
        print("1. demo_google_search()")
        print("2. demo_github_explore()")
        print("3. demo_website_info()")
        print("\nTo run demos, uncomment the functions below:\n")

        # Uncomment one of these to run:
        # demo_google_search()
        # demo_github_explore()
        # demo_website_info()

        print("""
NEXT STEPS:
───────────
1. Install dependencies:
   pip install -r requirements.txt

2. Run this script with a demo uncommented:
   python simple_browser_demo.py

3. Watch the browser automate tasks!

4. Try with your own websites:
   coordinator.step_by_step(
       goal="Your task here",
       initial_url="https://your-site.com",
       on_step=lambda info: print(info['step'])
   )

5. For AI-powered automation:
   export DEEPSEEK_API_KEY="your_key"
   python examples/quick_start.py
        """)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you have:")
        print("• Installed dependencies: pip install -r requirements.txt")
        print("• Chrome/Chromium browser installed")
        print("• Python 3.7+")
