from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in login_page.get_flash_message()


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("wrong", "wrong")

    assert "Your username is invalid!" in login_page.get_flash_message()