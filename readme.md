# Selenium Test Automation Demo

Simple Selenium + Pytest demo project built around the Page Object Model.

## Architecture

- `pages/` contains reusable page objects and shared page helpers.
- `tests/` contains the pytest test cases.
- `conftest.py` provides the shared `driver` fixture, `--headless` option, and failure screenshots.
- `requirements.txt` defines the Python dependencies.
- `.github/workflows/tests.yml` runs the suite in GitHub Actions on push.

The flow is:

1. Pytest loads `conftest.py` automatically.
2. The `driver` fixture starts Chrome for each test.
3. Tests call page object methods instead of raw Selenium commands.
4. If a test fails, a screenshot is saved in `screenshots/`.
5. The browser is closed after the test finishes.

What been done:

1. A clean Page Object Model structure
2. Shared pytest fixture setup in conftest.py
3. Real Selenium interaction with waits
4. Positive and negative test cases
5. Headless mode support
6. Failure screenshots
7. A passing suite

## Local Run

Run these commands from the repository root.

1. Create a virtual environment if needed:

	python3 -m venv .venv

2. Activate it:

	macOS/Linux:

	source .venv/bin/activate

3. Install dependencies:

	python -m pip install -r requirements.txt

4. Run the full suite with a visible browser:

	python -m pytest -q

5. Run in headless mode:

	python -m pytest -q --headless

6. Run a single test file:

	python -m pytest -q tests/test_login.py

## CI Run

The GitHub Actions workflow in [.github/workflows/tests.yml](.github/workflows/tests.yml) runs automatically on push to `main`.

In CI it:

- Uses Ubuntu and Python 3.12
- Installs dependencies from `requirements.txt`
- Runs `python -m pytest -q --headless`
- Uploads `screenshots/` as an artifact if tests fail

## Test Coverage

- Valid login
- Invalid login combinations
- Logout flow
- Dashboard visibility after login

## Testing Layers

1. Functional testing

Verifies features work as expected.

Examples:

- User logs in and should land on dashboard/secure area.
- Button click triggers the expected result.

In this project, Selenium simulates a real user in a browser to validate these flows.

2. Regression testing

Ensures new changes did not break existing features.

You rerun existing test cases automatically.

This is where automation helps most: instead of manually clicking through everything after each change, the scripts do it repeatedly and consistently.

3. Integration testing

Tests how components work together.

UI + real web app integration from login page to secure area (end-to-end user flow), especially in test_dashboard.py:13

Example:

- Frontend to backend to database flow works correctly.


Selenium can be used here, but integration coverage is often strengthened by combining UI checks with API assertions, mocks, or backend checks.

