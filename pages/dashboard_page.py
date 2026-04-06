from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")

    def is_logout_visible(self):
        return self.wait_for_element(*self.LOGOUT_BUTTON).is_displayed()