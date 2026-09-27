import allure
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver
from pages.calculator_page import SlowCalculatorPage


@pytest.fixture
def driver():
    chrome_driver = Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@allure.feature("Калькулятор с задержкой вычислений")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка арифметической операции сложения 7 + 8")
@allure.description(
    "Тест открывает калькулятор, "
    "устанавливает кастомное время задержки, "
    "вводит выражение 7 + 8 "
    "и проверяет корректность результата с учетом ожидания."
)
def test_slow_calculator_operation(driver: WebDriver) -> None:
    calc_page = SlowCalculatorPage(driver)

    calc_page.open()
    calc_page.set_delay("45")

    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    actual_result = calc_page.wait_for_result(
        expected_text="15", timeout=50)

    with allure.step(
            "Проверка соответствия фактического результата ожидаемому ('15')"):
        assert (
            actual_result == "15"
        ), f"Ожидался результат '15', но на экране: '{actual_result}'"
