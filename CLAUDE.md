# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**AI Agencies For Trading Forex** is a system for building autonomous AI agents that trade forex (foreign exchange) markets. The project enables creation, management, and execution of multiple AI trading agencies with coordinated strategies.

## Architecture Overview

### Key Components

The project is organized around these core abstractions:

- **Agencies**: Top-level autonomous entities that manage trading strategies and execution. Each agency encapsulates its own configuration, trading parameters, and decision-making logic.
- **Agents**: Individual AI agents within agencies that perform specific roles (analysis, execution, risk management, etc.).
- **Strategies**: Trading logic and decision patterns that agents execute. Strategies define entry/exit conditions, position sizing, and risk parameters.
- **Market Data Interface**: Real-time and historical forex data integration for technical analysis and decision making.
- **Execution Engine**: System responsible for executing trades, managing positions, and enforcing risk constraints.
- **Monitoring & Logging**: Real-time monitoring of agency activities, trade execution, and performance metrics.

### Design Patterns

- **Agent-based Architecture**: Use loosely coupled agents that communicate through defined interfaces, allowing independent development and testing.
- **Strategy Pattern**: Trading strategies are pluggable components that can be composed and switched at runtime.
- **Observer Pattern**: Agencies observe market events and trigger strategy evaluations and trade execution.
- **Risk-first Design**: Risk constraints and position limits are enforced at the execution layer, not just at the strategy layer.

## Development Setup

### Prerequisites
- Python 3.9+ (or Node.js 18+ if TypeScript is used)
- Git
- Virtual environment tool (venv or conda)

### Common Commands

When the project structure is implemented:

```bash
# Install dependencies
pip install -r requirements.txt

# Run linting
pylint src/ --disable=missing-docstring

# Run tests
pytest tests/ -v

# Run a single test
pytest tests/test_agency.py::test_agency_initialization -v

# Run type checking
mypy src/ --ignore-missing-imports

# Start development environment
python -m src.main

# Run with debug logging
DEBUG=1 python -m src.main
```

## Code Structure (Planned)

```
src/
  __init__.py
  main.py                    # Entry point
  config.py                  # Configuration loading and validation
  
  agencies/
    base.py                  # Agency base class and interface
    forex_agency.py          # Forex-specific agency implementation
    __init__.py
  
  agents/
    base.py                  # Agent base class
    analysis_agent.py        # Market analysis agent
    execution_agent.py       # Trade execution agent
    risk_agent.py            # Risk management agent
    __init__.py
  
  strategies/
    base.py                  # Strategy base class and interface
    technical_analysis.py    # Technical analysis strategies
    fundamental_analysis.py  # Fundamental analysis strategies
    __init__.py
  
  market_data/
    provider.py              # Abstract market data provider
    forex_provider.py        # Forex-specific data fetching
    cache.py                 # Data caching layer
    __init__.py
  
  execution/
    executor.py              # Trade execution engine
    position_manager.py      # Position tracking and management
    risk_validator.py        # Risk constraint validation
    __init__.py
  
  monitoring/
    logger.py                # Structured logging
    metrics.py               # Performance metrics tracking
    dashboard.py             # Real-time monitoring interface
    __init__.py

tests/
  unit/                      # Unit tests for individual components
  integration/               # Integration tests for agent interactions
  fixtures/                  # Test data and mock providers
```

## Key Architectural Decisions

1. **Asynchronous Execution**: Use async/await patterns for non-blocking market data fetching and order execution.
2. **Immutable Configuration**: Agency and strategy configurations are loaded once and treated as immutable during execution.
3. **Separation of Concerns**: Keep strategy logic (what to trade) separate from execution logic (how to trade).
4. **Auditability**: All trade decisions and executions must be logged with reasoning for analysis and compliance.
5. **Testability**: Use dependency injection to allow mocking of market data providers and execution engines for testing.

## Development Conventions

- **Naming**: Use descriptive names for agencies (e.g., `swing_trade_agency`, `scalp_trade_agency`). Agent roles should be clear (e.g., `TechnicalAnalysisAgent`, `ExecutionAgent`).
- **Configuration**: Use YAML or JSON for agency/strategy configuration. Environment variables for sensitive data (API keys, account credentials).
- **Error Handling**: Distinguish between recoverable errors (network issues, temporary data unavailability) and critical errors (position loss, execution failure).
- **Type Hints**: Use Python type hints throughout. Run mypy for static type checking.
- **Testing**: Aim for 80%+ code coverage. Use pytest with fixtures for market data and mock brokers.

## Important Notes

- **Risk Management**: This system handles real financial trading. All risk constraints must be tested thoroughly before production use.
- **Data Integrity**: Market data feeds must be validated. Duplicate, missing, or stale data can cause incorrect trading decisions.
- **Broker Integration**: Use broker APIs (e.g., MetaTrader 5, Alpaca, OANDA) with proper authentication and error handling.
- **Regulatory Compliance**: Ensure the system complies with relevant financial regulations in all operating jurisdictions.

## Git Workflow

Development happens on feature branches. Create branches from `main` with descriptive names like:
- `feature/agency-base-implementation`
- `feature/technical-analysis-strategy`
- `fix/position-sizing-edge-case`

Commit messages should be clear and reference specific components or strategies being modified.
