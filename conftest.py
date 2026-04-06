"""Pytest configuration for Selenium tests.

This file provides the shared browser fixture used by all tests, adds a
`--headless` command-line flag, and captures screenshots when a test fails.
Pytest discovers these hooks automatically because the file is named
`conftest.py`.
"""

import os
from datetime import datetime

import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run UI tests in headless Chrome",
    )


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture
def driver(request):
    options = Options()
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = ChromeWebDriver(service=service, options=options)
    if not request.config.getoption("--headless"):
        driver.maximize_window()

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{request.node.name}_{ts}.png"
        driver.save_screenshot(os.path.join("screenshots", file_name))

    driver.quit()