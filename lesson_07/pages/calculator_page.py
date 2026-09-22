from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SlowCalculatorPage:
    def __init__(self, driver, url=None):
        self.driver = driver
        # Исправлено: добавлен пропущенный слэш между строками
        self._url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        # Локаторы элементов страницы
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self):
        # Открывает страницу калькулятора.
        self.driver.get(self._url)

    def set_delay(self, seconds: str):
        # Очищает поле задержки и вводит новое значение.
        delay_element = self.driver.find_element(*self._delay_input)
        delay_element.clear()
        delay_element.send_keys(seconds)

    def click_button(self, text: str):
        # Находит кнопку на калькуляторе по тексту и кликает на нее.
        button_locator = (By.XPATH, f"//span[text()='{text}']")
        self.driver.find_element(*button_locator).click()

    def wait_for_result(self, expected_text: str, timeout: int = 50) -> str:
        # Ожидает появление ожидаемого текста
        # на экране калькулятора и возвращает его.
        wait = WebDriverWait(self.driver, timeout)
        err_msg = (
            f"Ошибка: Результат '{expected_text}' "
            f"не отобразился на экране за {timeout} сек."
        )

        # Динамически ждем изменения текста в элементе экрана
        # Исправлено: запятая возвращена на предыдущую строку
        wait.until(
            EC.text_to_be_present_in_element(
                self._result_screen, expected_text
            ),
            err_msg
        )
        return self.driver.find_element(*self._result_screen).text
