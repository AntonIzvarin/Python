import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)
        self._checkout_button: tuple[str, str] = (By.CSS_SELECTOR, "#checkout")

    @allure.step("Нажать кнопку продолжения оформления заказа (Checkout)")
    def click_checkout(self) -> None:
        """
        Кликает по кнопке оформления заказа для перехода к заполнению формы.
        """
        self.wait.until(
            EC.element_to_be_clickable(self._checkout_button)
        ).click()
