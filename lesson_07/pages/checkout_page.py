from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._first_name = (By.CSS_SELECTOR, "#first-name")
        self._last_name = (By.CSS_SELECTOR, "#last-name")
        self._postal_code = (By.CSS_SELECTOR, "#postal-code")
        self._continue_button = (By.CSS_SELECTOR, "#continue")
        self._total_label = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_checkout_form(
            self, first_name: str, last_name: str, zip_code: str):
        self.wait.until(
            EC.presence_of_element_located(self._first_name)
        ).send_keys(first_name)
        self.driver.find_element(*self._last_name).send_keys(last_name)
        self.driver.find_element(*self._postal_code).send_keys(zip_code)

    def click_continue(self):
        # presence_of_element_located работает стабильнее при переходе в Safari
        self.wait.until(
            EC.presence_of_element_located(self._continue_button)
        ).click()

    def get_total_price_text(self) -> str:
        # Ожидаем появления элемента в DOM
        total_element = self.wait.until(
            EC.presence_of_element_located(self._total_label),
            "Элемент с итоговой ценой не отобразился"
        )
        # Ожидаем, что текст цены подгрузился во внутренний текст
        self.wait.until(
            EC.text_to_be_present_in_element(self._total_label, "$")
        )
        return total_element.text
