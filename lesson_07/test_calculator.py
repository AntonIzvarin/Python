import pytest
from selenium.webdriver import Chrome
from pages.calculator_page import SlowCalculatorPage


@pytest.fixture
def driver():
    # Фикстура для инициализации и закрытия браузера Google Chrome.
    chrome_driver = Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_slow_calculator_operation(driver):
    # Инициализируем Page Object
    calc_page = SlowCalculatorPage(driver)

    # Шаг 1: Открыть страницу калькулятора через Page Object
    calc_page.open()

    # Шаг 2: Ввести значение 45 в поле задержки
    calc_page.set_delay("45")

    # Шаг 3: Нажать кнопки: 7, +, 8, =
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    # Шаг 4: Проверить (assert),
    # что в окне отобразится результат 15 через 45 секунд
    # Передаем запас по времени (50 секунд),
    # чтобы компенсировать задержку калькулятора
    actual_result = calc_page.wait_for_result(expected_text="15", timeout=50)

    assert (
        actual_result == "15"
    ), f"Ожидался результат '15', но на экране: '{actual_result}'"
