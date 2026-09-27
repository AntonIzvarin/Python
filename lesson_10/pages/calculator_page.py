import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class SlowCalculatorPage:
    def __init__(self, driver: WebDriver, url: str = None) -> None:
        self.driver: WebDriver = driver
        self._url: str = (
            "https://bonigarcia.dev"
            "selenium-webdriver-java/slow-calculator.html"
        )
        self._delay_input: tuple[str, str] = (By.CSS_SELECTOR, "#delay")
        self._result_screen: tuple[str, str] = (By.CSS_SELECTOR, ".screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает веб-страницу калькулятора в браузере."""
        self.driver.get(self._url)

    @allure.step("Установить задержку вычислений: {seconds} сек.")
    def set_delay(self, seconds: str) -> None:
        """
        Очищает поле ввода задержки и устанавливает новое текстовое значение.
        """
        delay_element = self.driver.find_element(*self._delay_input)
        delay_element.clear()
        delay_element.send_keys(seconds)

    @allure.step("Нажать на кнопку калькулятора: '{text}'")
    def click_button(self, text: str) -> None:
        """
        Находит кнопку на виртуальном калькуляторе по тексту и кликает на нее.
        """
        button_locator = (By.XPATH, f"//span[text()='{text}']")
        self.driver.find_element(*button_locator).click()

    @allure.step("Ожидать появление результата: '{expected_text}'")
    def wait_for_result(self, expected_text: str, timeout: int = 50) -> str:
        """
        Ожидает появление ожидаемого текста на экране калькулятора.
        Возвращает итоговый текст экрана после завершения анимации.
        """
        wait = WebDriverWait(self.driver, timeout)
        err_msg = (
            f"Ошибка: Результат '{expected_text}' "
            f"не отобразился на экране за {timeout} сек."
        )

        wait.until(
            EC.text_to_be_present_in_element(
                self._result_screen, expected_text
            ),
            err_msg
        )
        return self.driver.find_element(*self._result_screen).text
