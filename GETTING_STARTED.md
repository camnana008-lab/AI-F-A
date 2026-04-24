# Getting Started with AI Automation System

## 🚀 5-Minute Quick Start

### 1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 2. **Get API Key (Optional for basic browser automation)**
- Go to https://deepseek.com/api
- Get your API key
- Set it: `export DEEPSEEK_API_KEY="your_key"`

### 3. **Run Preview**
```bash
# See the system overview
python preview_demo.py

# See working examples (no API needed)
python test_system.py

# Simple browser automation example
python simple_browser_demo.py
```

---

## 🎯 Three Ways to Use

### **Option 1: Direct Browser Control (No AI)**
```python
from src.ai_automation.executor.browser_engine import BrowserEngine

browser = BrowserEngine(headless=False)
browser.start()
browser.navigate("https://google.com")
browser.type_text("input[name='q']", "AI automation")
browser.click("input[name='btnK']")
browser.screenshot("result.png")
browser.stop()
```

### **Option 2: Simple Automation (No API)**
```python
from src.ai_automation.executor.browser_engine import BrowserEngine

# Just use the browser - no AI needed!
browser = BrowserEngine()
browser.start()
# ... your browser actions
browser.stop()
```

### **Option 3: AI-Powered Automation (Requires API)**
```python
from src.ai_automation import AIAutomationCoordinator

coordinator = AIAutomationCoordinator()

result = coordinator.step_by_step(
    goal="Find and click the download button",
    initial_url="https://example.com",
    on_step=lambda info: print(f"Step {info['step']}")
)

print(f"Success: {result['success']}")
```

---

## 📁 Project Structure

```
AI-F-A/
├── src/ai_automation/
│   ├── brain/           # DeepSeek reasoning (AI)
│   ├── arm/             # Code execution
│   ├── executor/        # Browser control (Selenium)
│   └── coordinator.py   # Main orchestrator
├── examples/            # Example scripts
├── preview_demo.py      # System preview
├── test_system.py       # Working examples
├── simple_browser_demo.py # Simple automation
└── requirements.txt     # Dependencies
```

---

## 🎮 Common Use Cases

### **Game Automation**
```python
coordinator = AIAutomationCoordinator()
result = coordinator.step_by_step(
    goal="Play the game and reach level 10",
    initial_url="https://game.example.com"
)
```

### **Trading Automation**
```python
coordinator = AIAutomationCoordinator()
result = coordinator.step_by_step(
    goal="Log in and place a buy order for EUR/USD",
    initial_url="https://trading.example.com"
)
```

### **Data Extraction**
```python
browser = BrowserEngine(headless=True)
browser.start()
browser.navigate("https://data.example.com")
prices = browser.find_elements("td.price")
for price in prices:
    print(price.text)
browser.stop()
```

### **Form Filling**
```python
browser = BrowserEngine()
browser.start()
browser.navigate("https://form.example.com")
browser.type_text("input#name", "John")
browser.type_text("input#email", "john@example.com")
browser.click("button#submit")
browser.stop()
```

---

## 🔧 Configuration

### **Headless Mode (Invisible Browser)**
```python
coordinator = AIAutomationCoordinator(headless=True)
```

### **Adjust Timeouts**
```python
coordinator.browser.wait_timeout = 20  # seconds
```

### **Max Steps**
```python
coordinator.max_steps = 50
```

---

## 📚 Available Methods

### **BrowserEngine Methods**
| Method | Purpose |
|--------|---------|
| `navigate(url)` | Go to URL |
| `click(selector)` | Click element |
| `type_text(selector, text)` | Type in field |
| `get_text(selector)` | Get element text |
| `screenshot(filename)` | Take screenshot |
| `wait_for_element(selector)` | Wait for element |
| `find_elements(selector)` | Find multiple elements |
| `scroll(direction)` | Scroll page |
| `get_page_title()` | Get page title |
| `get_page_url()` | Get current URL |

### **Coordinator Methods**
| Method | Purpose |
|--------|---------|
| `execute_goal(goal, url)` | Run automation once |
| `step_by_step(goal, url, callback)` | Run with step monitoring |
| `get_status()` | Get current status |

### **DeepSeek Methods**
| Method | Purpose |
|--------|---------|
| `think(task, context)` | Get reasoning |
| `analyze(observation)` | Analyze data |
| `plan(goal)` | Create action plan |

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Chrome not found | Install: `sudo apt install chromium-browser` |
| Import error | Run: `pip install -r requirements.txt` |
| API key not found | Set: `export DEEPSEEK_API_KEY="key"` |
| Timeout errors | Increase: `coordinator.browser.wait_timeout` |
| Element not found | Use browser DevTools (F12) to find selector |

---

## 💡 Tips & Tricks

### **Finding CSS Selectors**
1. Open browser DevTools (F12)
2. Right-click element → Inspect
3. Copy the selector
4. Use in your code

### **Testing Selectors**
```python
browser.wait_for_element("your.selector")
```

### **Debugging**
```python
# Take screenshot at each step
def debug_step(info):
    print(f"Step {info['step']}: {info['action']}")
    browser.screenshot(f"step_{info['step']}.png")

result = coordinator.step_by_step(goal="...", on_step=debug_step)
```

### **Using Chrome DevTools**
```python
# Get page source for inspection
source = browser.get_page_source()
print(source[:500])
```

---

## 📖 Example Files

- **`preview_demo.py`** - System architecture overview
- **`test_system.py`** - Real working examples
- **`simple_browser_demo.py`** - Simple automation demo
- **`examples/quick_start.py`** - Quick start demo
- **`examples/trading_example.py`** - Trading automation
- **`examples/example_game_automation.py`** - Game automation

---

## 🔑 Getting DeepSeek API Key

1. Visit https://deepseek.com/api
2. Sign up / Log in
3. Generate API key
4. Set environment variable:
   ```bash
   export DEEPSEEK_API_KEY="sk-..."
   ```

---

## 🎓 Learning Path

1. **Start here**: Run `python simple_browser_demo.py`
2. **Try examples**: Run `python examples/quick_start.py`
3. **Create simple automation**: Edit `simple_browser_demo.py`
4. **Get API key**: https://deepseek.com/api
5. **Try AI automation**: Run coordinator examples
6. **Build your bot**: Create your own script

---

## ⚡ Quick Commands Reference

```bash
# View system
python preview_demo.py

# See examples
python test_system.py

# Run simple browser automation
python simple_browser_demo.py

# Install dependencies
pip install -r requirements.txt

# Set API key
export DEEPSEEK_API_KEY="your_key"

# Run AI examples
python examples/quick_start.py
python examples/trading_example.py
```

---

## 🎯 What's Next?

1. ✅ Run `python preview_demo.py` to see the system
2. ✅ Run `python simple_browser_demo.py` to try browser automation
3. ✅ Get DeepSeek API key from https://deepseek.com/api
4. ✅ Run `python examples/quick_start.py` for AI automation
5. ✅ Create your own automation script!

---

## 📞 Support

- Check examples for patterns
- Read `README_AI_AUTOMATION.md` for detailed docs
- Review error messages for clues
- Test selectors with browser DevTools

---

## 🎉 You're Ready!

Your AI Automation System is ready to go. Start with the simple examples and build from there. Happy automating! 🚀
