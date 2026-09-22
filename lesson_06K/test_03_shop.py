from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shopping():
    # 1. Открываем сайт магазина в Safari
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.get("https://saucedemo.com")

    # Создаем объект явного ожидания на 10 секунд
    wait = WebDriverWait(driver, 10)

    try:
        # 2. Авторизуемся под пользователем standard_user
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name"))
        ).send_keys("standard_user")
        driver.find_element(
            By.CSS_SELECTOR, "#password"
        ).send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "#login-button").click()

        # 3. Добавляем в корзину товары
        wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
            )
        ).click()
        wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
            )
        ).click()
        wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
            )
        ).click()

        # 4. Переходим в корзину
        driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

        # 5. Нажимаем кнопку Checkout
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
        ).click()

        # 6. Заполняем форму персональными данными
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "#first-name"))
        ).send_keys("Ivan")
        (driver.find_element(By.CSS_SELECTOR, "#last-name")
         .send_keys("Petrov"))
        (driver.find_element(By.CSS_SELECTOR, "#postal-code")
         .send_keys("123456"))

        # 7. Нажимаем кнопку Continue через ожидание кликабельности
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#continue"))
        ).click()

        # 8. Ожидаем появления блока финальной стоимости и считываем Total
        total_element = wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, ".summary_total_label"
            )),
            "Элемент с итоговой ценой не отобразился",
        )
        total_text = total_element.text

        # 9. Проверяем (assert), что итоговая сумма равна $58.29
        assert (
            "$58.29" in total_text
        ), f"Ожидалась сумма $58.29, но на странице: '{total_text}'"

    finally:
        # Браузер закроется гарантированно
        driver.quit()
