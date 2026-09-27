import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)
        self._url: str = "https://saucedemo.com"
        self._username_input: tuple[str, str] = (
            By.CSS_SELECTOR, "#user-name")
        self._password_input: tuple[str, str] = (
            By.CSS_SELECTOR, "#password")
        self._login_button: tuple[str, str] = (
            By.CSS_SELECTOR, "#login-button")

    @allure.step("Открыть главную страницу магазина")
    def open(self) -> None:
        """
        Загружает стартовую страницу авторизации магазина.
        """
        self.driver.get(self._url)

    @allure.step("Авторизоваться пользователем: '{username}'")
    def login(self, username: str, password: str) -> None:
        """Выполняет полный цикл авторизации пользователя в магазине."""
        self.wait.until(
            EC.presence_of_element_located(self._username_input)
        ).send_keys(username)
        self.driver.find_element(*self._password_input).send_keys(password)
        self.wait.until(
            EC.element_to_be_clickable(self._login_button)
        ).click()
