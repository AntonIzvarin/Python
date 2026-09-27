import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)
        self._first_name: tuple[str, str] = (By.CSS_SELECTOR, "#first-name")
        self._last_name: tuple[str, str] = (By.CSS_SELECTOR, "#last-name")
        self._postal_code: tuple[str, str] = (By.CSS_SELECTOR, "#postal-code")
        self._continue_button: tuple[str, str] = (By.CSS_SELECTOR, "#continue")
        self._total_label: tuple[str, str] = (
            By.CSS_SELECTOR, ".summary_total_label"
        )

    @allure.step(
        "Заполнить форму заказа данными: "
        "{first_name} {last_name}, ZIP: {zip_code}"
    )
    def fill_checkout_form(
            self, first_name: str, last_name: str, zip_code: str
    ) -> None:
        """
        Заполняет персональные данные покупателя на странице оформления.
        """
        self.wait.until(
            EC.presence_of_element_located(self._first_name)
        ).send_keys(first_name)
        self.driver.find_element(*self._last_name).send_keys(last_name)
        self.driver.find_element(*self._postal_code).send_keys(zip_code)

    @allure.step("Нажать кнопку 'Continue' для перехода к деталям оплаты")
    def click_continue(self) -> None:
        """
        Подтверждает форму персональных данных.
        """
        self.wait.until(
            EC.element_to_be_clickable(self._continue_button)
        ).click()

    @allure.step(
        "Получить итоговую стоимость заказа")
    def get_total_price_text(self) -> str:
        """
        Дожидается загрузки стоимости
        и возвращает полную текстовую строку цены.
        """
        total_element = self.wait.until(
            EC.presence_of_element_located(self._total_label),
            "Элемент с итоговой ценой не отобразился"
        )
        self.wait.until(
            EC.text_to_be_present_in_element(self._total_label, "$")
        )
        return total_element.text
