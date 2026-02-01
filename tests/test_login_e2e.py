import pytest
from pages.login_page import LoginPage
import allure


@pytest.mark.smoke
@pytest.mark.positive
@allure.title("Успешный логин с валидными данными")
@allure.description("Проверка входа пользователя standard_user")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.positive
def test_login_positive(driver):
    ...

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
@allure.title("Ошибка логина при неверном пароле")
@allure.description("Проверка валидации при некорректном пароле")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.negative
def test_login_negative_invalid_password(driver):
    ...

def test_login_negative_invalid_password(driver):
    page = LoginPage(driver)
    page.open()

    page.login(
        username="standard_user",
        password="wrong_password"
    )

    assert page.is_error_displayed()
