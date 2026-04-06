# Selenium Test Automation Demo

## Tech Stack
- Python
- Selenium
- Pytest

## Features
- Functional tests (login success/failure)
- Basic integration flow (login → dashboard)
- Page Object Model (POM) design

## How to run

```bash
pip install -r requirements.txt
pytest

.venv/bin/python -m pytest -q

without view:

.venv/bin/python -m pytest -q --headless

End-to-end flow in your project:

1. You run pytest
2. Pytest loads conftest.py
3. For each test needing driver, fixture starts browser
4. Test executes Selenium steps
5. On failure, screenshot saved
6. Browser quits

What been done:

1. A clean Page Object Model structure
2. Shared pytest fixture setup in conftest.py
3. Real Selenium interaction with waits
4. Positive and negative test cases
5. Headless mode support
6. Failure screenshots
7. A passing suite