from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._url = "https://saucedemo.com"
        self._username_input = (By.CSS_SELECTOR, "#user-name")
        self._password_input = (By.CSS_SELECTOR, "#password")
        self._login_button = (By.CSS_SELECTOR, "#login-button")

    def open(self):
        self.driver.get(self._url)

    def login(self, username: str, password: str):
        self.wait.until(
            EC.presence_of_element_located(self._username_input)
        ).send_keys(username)
        self.driver.find_element(*self._password_input).send_keys(password)
        # Ожидаем кликабельности кнопки Login для исключения пропуска клика
        self.wait.until(
            EC.element_to_be_clickable(self._login_button)
        ).click()
