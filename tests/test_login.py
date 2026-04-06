import pytest

from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in login_page.get_flash_message()


@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        ("wrong", "wrong", "Your username is invalid!"),
        ("tomsmith", "wrong", "Your password is invalid!"),
        ("", "", "Your username is invalid!"),
    ],
)
def test_invalid_login_combinations(driver, username, password, expected_message):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    assert expected_message in login_page.get_flash_message()