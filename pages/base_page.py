from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        self.wait_for_clickable(by, value).click()

    def type(self, by, value, text):
        element = self.find(by, value)
        element.clear()
        element.send_keys(text)

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def wait_for_clickable(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def current_url(self):
        return self.driver.current_url

    def wait_for_url_contains(self, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def is_url_contains(self, text, timeout=10):
        try:
            return self.wait_for_url_contains(text, timeout)
        except TimeoutException:
            return False