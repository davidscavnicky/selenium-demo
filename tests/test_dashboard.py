from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_dashboard_access(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    dashboard = DashboardPage(driver)
    assert dashboard.is_logout_visible()