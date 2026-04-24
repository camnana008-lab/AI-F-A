"""Browser automation engine for web-based tasks."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from typing import Optional, Any, Tuple
from pathlib import Path


class BrowserEngine:
    """Handles all browser automation tasks."""

    def __init__(self, headless: bool = False):
        """Initialize browser engine.

        Args:
            headless: Run browser in headless mode
        """
        self.driver = None
        self.headless = headless
        self.wait_timeout = 10

    def start(self) -> bool:
        """Start the browser.

        Returns:
            True if browser started successfully
        """
        try:
            options = webdriver.ChromeOptions()
            if self.headless:
                options.add_argument("--headless")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])

            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            return True
        except Exception as e:
            print(f"Failed to start browser: {e}")
            return False

    def stop(self):
        """Stop the browser."""
        if self.driver:
            self.driver.quit()

    def navigate(self, url: str) -> bool:
        """Navigate to a URL.

        Args:
            url: URL to navigate to

        Returns:
            True if navigation succeeded
        """
        try:
            self.driver.get(url)
            time.sleep(2)
            return True
        except Exception as e:
            print(f"Navigation failed: {e}")
            return False

    def click(self, selector: str, by: By = By.CSS_SELECTOR) -> bool:
        """Click an element.

        Args:
            selector: Element selector
            by: Selector type (CSS_SELECTOR, ID, XPATH, etc.)

        Returns:
            True if click succeeded
        """
        try:
            element = WebDriverWait(self.driver, self.wait_timeout).until(
                EC.element_to_be_clickable((by, selector))
            )
            element.click()
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Click failed: {e}")
            return False

    def type_text(self, selector: str, text: str, by: By = By.CSS_SELECTOR) -> bool:
        """Type text into an element.

        Args:
            selector: Element selector
            text: Text to type
            by: Selector type

        Returns:
            True if typing succeeded
        """
        try:
            element = WebDriverWait(self.driver, self.wait_timeout).until(
                EC.presence_of_element_located((by, selector))
            )
            element.clear()
            element.send_keys(text)
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Type text failed: {e}")
            return False

    def get_text(self, selector: str, by: By = By.CSS_SELECTOR) -> Optional[str]:
        """Get text from an element.

        Args:
            selector: Element selector
            by: Selector type

        Returns:
            Text content or None
        """
        try:
            element = WebDriverWait(self.driver, self.wait_timeout).until(
                EC.presence_of_element_located((by, selector))
            )
            return element.text
        except Exception as e:
            print(f"Get text failed: {e}")
            return None

    def screenshot(self, filename: str = "screenshot.png") -> bool:
        """Take a screenshot.

        Args:
            filename: Output filename

        Returns:
            True if screenshot succeeded
        """
        try:
            self.driver.save_screenshot(filename)
            return True
        except Exception as e:
            print(f"Screenshot failed: {e}")
            return False

    def wait_for_element(self, selector: str, by: By = By.CSS_SELECTOR) -> bool:
        """Wait for element to appear.

        Args:
            selector: Element selector
            by: Selector type

        Returns:
            True if element appeared
        """
        try:
            WebDriverWait(self.driver, self.wait_timeout).until(
                EC.presence_of_element_located((by, selector))
            )
            return True
        except Exception as e:
            print(f"Wait failed: {e}")
            return False

    def find_elements(self, selector: str, by: By = By.CSS_SELECTOR) -> list:
        """Find multiple elements.

        Args:
            selector: Element selector
            by: Selector type

        Returns:
            List of elements
        """
        try:
            return self.driver.find_elements(by, selector)
        except Exception as e:
            print(f"Find elements failed: {e}")
            return []

    def get_page_title(self) -> Optional[str]:
        """Get page title.

        Returns:
            Page title or None
        """
        try:
            return self.driver.title
        except Exception as e:
            print(f"Get title failed: {e}")
            return None

    def get_page_url(self) -> Optional[str]:
        """Get current page URL.

        Returns:
            Current URL or None
        """
        try:
            return self.driver.current_url
        except Exception as e:
            print(f"Get URL failed: {e}")
            return None

    def scroll(self, direction: str = "down", amount: int = 500):
        """Scroll the page.

        Args:
            direction: "up" or "down"
            amount: Pixels to scroll
        """
        try:
            if direction == "down":
                self.driver.execute_script(f"window.scrollBy(0, {amount})")
            elif direction == "up":
                self.driver.execute_script(f"window.scrollBy(0, -{amount})")
            time.sleep(0.5)
        except Exception as e:
            print(f"Scroll failed: {e}")

    def execute_script(self, script: str) -> Any:
        """Execute JavaScript.

        Args:
            script: JavaScript code

        Returns:
            Script result
        """
        try:
            return self.driver.execute_script(script)
        except Exception as e:
            print(f"Execute script failed: {e}")
            return None

    def get_page_source(self) -> Optional[str]:
        """Get page HTML source.

        Returns:
            Page HTML or None
        """
        try:
            return self.driver.page_source
        except Exception as e:
            print(f"Get source failed: {e}")
            return None

    def wait(self, seconds: float):
        """Wait for specified seconds.

        Args:
            seconds: Seconds to wait
        """
        time.sleep(seconds)
