# AI Automation System - DeepSeek Brain + Open Interpreter Arm

A modular AI automation system that combines **DeepSeek** (brain/reasoning) with **Open Interpreter** (arm/execution) for intelligent browser control, gaming automation, and trading tasks.

## Architecture

```
┌─────────────────────────────────────────┐
│         DeepSeek (Brain)                │
│  Reasoning, Planning, Decision Making   │
└──────────────┬──────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────┐
│  AI Coordination Coordinator             │
│  Orchestrates brain-arm interaction      │
└──────────────┬──────────────────────────┘
               │
               ↓
┌──────────────────────────────────────────┐
│    Open Interpreter (Arm)                │
│  Code Execution (Python, Bash)           │
└──────────────┬──────────────────────────┘
               │
               ↓
┌──────────────────────────────────────────┐
│    Browser Engine (Selenium)             │
│  Clicks, types, navigates, extracts data │
└──────────────────────────────────────────┘
```

## Components

### 1. **DeepSeekBrain** (`src/ai_automation/brain/deepseek_brain.py`)
Handles reasoning and decision making using DeepSeek API.

**Features:**
- Think about tasks and generate action plans
- Analyze observations and extract key information
- Maintain conversation history for context awareness
- Generate step-by-step plans to achieve goals

**Usage:**
```python
from src.ai_automation.brain import DeepSeekBrain

brain = DeepSeekBrain(api_key="your_key")
plan = brain.plan("Play a browser game and reach level 5")
analysis = brain.analyze("Game screen shows level 3 with 100 health")
```

### 2. **InterpreterArm** (`src/ai_automation/arm/interpreter_arm.py`)
Executes code and commands to control the system.

**Features:**
- Execute Python code
- Execute bash commands
- Generate and run Selenium browser control code
- Track execution history

**Usage:**
```python
from src.ai_automation.arm import InterpreterArm

arm = InterpreterArm()
result = arm.execute_python("print('Hello from interpreter')")
result = arm.execute_browser_control("click", selector="button#play")
```

### 3. **BrowserEngine** (`src/ai_automation/executor/browser_engine.py`)
Selenium-based browser automation with high-level methods.

**Features:**
- Navigate to URLs
- Click elements
- Type text
- Extract text
- Take screenshots
- Wait for elements
- Execute JavaScript
- Scroll pages

**Usage:**
```python
from src.ai_automation.executor.browser_engine import BrowserEngine

browser = BrowserEngine(headless=False)
browser.start()
browser.navigate("https://example.com")
browser.click("button#submit")
text = browser.get_text("div.result")
browser.screenshot("result.png")
browser.stop()
```

### 4. **AIAutomationCoordinator** (`src/ai_automation/coordinator.py`)
Orchestrates the brain-arm coordination.

**Features:**
- Execute goals with automatic step-by-step coordination
- Real-time step callbacks for monitoring
- Context awareness
- Goal achievement detection
- Status tracking

**Usage:**
```python
from src.ai_automation import AIAutomationCoordinator

coordinator = AIAutomationCoordinator()

def on_step(info):
    print(f"Step {info['step']}: {info['action']}")

result = coordinator.step_by_step(
    goal="Play the game and reach level 5",
    initial_url="https://game.example.com",
    on_step=on_step
)
```

## Installation

1. **Clone the repository:**
```bash
git clone <repo-url>
cd AI-F-A
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
```bash
cp .env.example .env
# Edit .env and add your DEEPSEEK_API_KEY
export $(cat .env | xargs)
```

## Getting Started

### Quick Demo
```bash
python examples/quick_start.py
```

This runs two demonstrations:
1. Direct browser automation (no AI)
2. AI-coordinated browser automation

### Basic Example

```python
from src.ai_automation import AIAutomationCoordinator

# Create coordinator
coordinator = AIAutomationCoordinator(headless=False)

# Execute a goal
result = coordinator.execute_goal(
    goal="Find and click the start button",
    initial_url="https://example.com/game"
)

print(f"Success: {result['success']}")
print(f"Steps: {result['steps']}")
```

### With Step Monitoring

```python
coordinator = AIAutomationCoordinator()

def monitor_step(step_info):
    print(f"Step {step_info['step']}: {step_info['action']}")
    print(f"Result: {step_info['observation']}")

result = coordinator.step_by_step(
    goal="Your goal here",
    initial_url="https://example.com",
    on_step=monitor_step
)
```

## Use Cases

### 1. **Browser Game Automation**
```python
result = coordinator.step_by_step(
    goal="Play the game: click buttons, collect items, reach level 10",
    initial_url="https://game.example.com",
    on_step=lambda info: print(f"Step {info['step']}: {info['observation']}")
)
```

### 2. **Trading Automation**
```python
result = coordinator.step_by_step(
    goal="Log in, analyze forex prices, place a buy order for EUR/USD",
    initial_url="https://trading.example.com",
    on_step=monitor_trading_step
)
```

### 3. **Data Extraction**
```python
browser = BrowserEngine(headless=True)
browser.start()
browser.navigate("https://data.example.com")
data = browser.get_text("table.results")
browser.stop()
```

### 4. **Form Filling**
```python
browser.navigate("https://form.example.com")
browser.type_text("input#name", "John Doe")
browser.type_text("input#email", "john@example.com")
browser.click("button#submit")
```

## Configuration

### DeepSeek API
Get your API key from: https://deepseek.com/api

Set environment variable:
```bash
export DEEPSEEK_API_KEY="sk-..."
```

### Browser Settings
In code:
```python
coordinator = AIAutomationCoordinator(
    deepseek_api_key="your-key",
    headless=False  # Set to True to run headless
)
```

### Timeouts and Retries
Modify in respective classes:
- BrowserEngine: `wait_timeout` (default: 10 seconds)
- AIAutomationCoordinator: `max_steps` (default: 20)
- InterpreterArm: Timeout in `execute_python` (default: 30s)

## Examples

See `examples/` directory for complete examples:
- `quick_start.py` - Quick start demo
- `example_game_automation.py` - Game automation patterns
- `example_trading.py` - Trading automation (coming soon)

## Project Structure

```
src/
  ai_automation/
    __init__.py
    coordinator.py           # Main orchestrator
    brain/
      deepseek_brain.py     # DeepSeek reasoning
    arm/
      interpreter_arm.py    # Code execution
    executor/
      browser_engine.py     # Browser control
examples/
  quick_start.py
  example_game_automation.py
tests/
.env.example
requirements.txt
README_AI_AUTOMATION.md
```

## Advanced Usage

### Custom Action Implementation
```python
class CustomCoordinator(AIAutomationCoordinator):
    def _execute_action(self, action: str) -> bool:
        if action.startswith("custom:"):
            custom_cmd = action.replace("custom:", "").strip()
            return self.handle_custom_action(custom_cmd)
        return super()._execute_action(action)
```

### Integration with Other LLMs
Replace DeepSeekBrain with another LLM:

```python
class CustomBrain:
    def think(self, task, context):
        # Your LLM integration here
        pass

coordinator = AIAutomationCoordinator()
coordinator.brain = CustomBrain()
```

### Headless Execution
```python
coordinator = AIAutomationCoordinator(headless=True)
result = coordinator.execute_goal("your goal", "https://example.com")
```

## Limitations & Notes

1. **DeepSeek API**: Requires valid API key and active internet
2. **Browser Automation**: Works with modern web applications supporting Selenium
3. **Execution Safety**: Only run code from trusted sources
4. **Rate Limiting**: DeepSeek API may have rate limits
5. **JavaScript Heavy Sites**: Some JS-heavy sites may need additional waits

## Troubleshooting

### "DEEPSEEK_API_KEY not found"
```bash
export DEEPSEEK_API_KEY="your-key-here"
```

### Browser won't start
```python
# Check that Chrome is installed
# On Ubuntu: sudo apt-get install chromium-browser
# On Mac: brew install chromium
```

### Timeout errors
Increase timeout:
```python
coordinator.browser.wait_timeout = 20
coordinator.max_steps = 30
```

### Element not found
Use browser console to inspect:
```python
browser.execute_script("console.log(document.querySelectorAll('button'))")
```

## Contributing

To add new features:
1. Create feature branch
2. Add tests in `tests/`
3. Update documentation
4. Submit pull request

## License

[Add your license here]

## Support

For issues or questions:
- Check examples/
- Review error messages in logs
- Verify API key is valid
- Ensure dependencies are installed

## References

- [DeepSeek API Docs](https://deepseek.com/api)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Open Interpreter](https://openinterpreter.com/)
