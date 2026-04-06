from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_dashboard_access(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    dashboard = DashboardPage(driver)
    assert dashboard.is_logout_visible()


def test_dashboard_url_after_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    dashboard = DashboardPage(driver)
    assert dashboard.is_open()


def test_logout_returns_to_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    dashboard = DashboardPage(driver)
    dashboard.logout()

    assert login_page.is_open()
    assert "You logged out of the secure area!" in login_page.get_flash_message()