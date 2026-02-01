from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        ).send_keys(username)

        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_error_displayed(self) -> bool:
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).is_displayed()

@allure.step("Открываем страницу логина SauceDemo")
def open(self):
    self.driver.get(self.URL)


@allure.step("Логинимся пользователем: {username}")
def login(self, username: str, password: str):
    self.wait.until(
        EC.visibility_of_element_located(self.USERNAME)
    ).send_keys(username)

    self.driver.find_element(*self.PASSWORD).send_keys(password)
    self.driver.find_element(*self.LOGIN_BUTTON).click()
