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


@pytest.mark.parametrize(
    "username,expected_message",
    [
        ("tomsmith ", "Your username is invalid!"),
        (" TOMSMITH", "Your username is invalid!"),
        ("tomsmith!", "Your username is invalid!"),
    ],
)
def test_username_edge_cases(driver, username, expected_message):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, "SuperSecretPassword!")

    assert expected_message in login_page.get_flash_message()


@pytest.mark.parametrize(
    "password,expected_message",
    [
        ("SuperSecretPassword! ", "Your password is invalid!"),
        ("supersecretpassword!", "Your password is invalid!"),
        ("123456", "Your password is invalid!"),
    ],
)
def test_password_edge_cases(driver, password, expected_message):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", password)

    assert expected_message in login_page.get_flash_message()