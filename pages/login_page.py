from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.type(*self.USERNAME, username)
        self.type(*self.PASSWORD, password)
        self.click(*self.LOGIN_BUTTON)

    def get_flash_message(self):
        return self.wait_for_element(*self.FLASH_MESSAGE).text

    def is_open(self):
        return self.is_url_contains("/login")