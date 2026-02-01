import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.positive
def test_login_positive(driver):
    page = LoginPage(driver)
    page.open()

    page.login(
        username="standard_user",
        password="secret_sauce"
    )

    assert "inventory" in driver.current_url


@pytest.mark.smoke
@pytest.mark.negative
def test_login_negative_invalid_password(driver):
    page = LoginPage(driver)
    page.open()

    page.login(
        username="standard_user",
        password="wrong_password"
    )

    assert page.is_error_displayed()
