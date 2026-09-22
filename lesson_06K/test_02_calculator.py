from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    # 1. Открываем страницу строго в Google Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(url)

    # 2. Находим поле ввода задержки по указанному локатору #delay
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")

    # Очищаем дефолтное значение и вводим 45
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажимаем на кнопки калькулятора через точные XPATH-локаторы
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # 4. Инициализируем явное ожидание на 50 секунд
    wait = WebDriverWait(driver, 50)

    # 5. Динамически ждем, пока в элементе экрана появится текст "15"
    err_msg = "Ошибка: Результат '15' не отобразился на экране."
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"),
        err_msg,
    )

    # 6. Финальная проверка (assert)
    result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert (
            result_text == "15"
    ), f"Ожидался результат '15', но на экране: '{result_text}'"

    # 7. Закрываем браузер
    driver.quit()
