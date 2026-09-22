from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_submission():
    # 1. Открываем страницу "https://httpbin.qa-territory.online/forms/post"
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    sleep(3)

    # 2. Находим поле ввода с названием custname
    custname_field = driver.find_element(By.NAME, "custname")

    # 3. Вводим имя в поле
    custname_field.send_keys("Anton Izvarin")
    sleep(3)

    # 4. Находим кнопку Submit и нажимаем на нее
    submit_button = driver.find_element(By.CSS_SELECTOR,
                                        "button[type='submit']")
    submit_button.click()
    sleep(3)

    # Проверяем, что перешли на страницу формы /post
    assert "/post" in driver.current_url, (
        f"Ошибка! Ожидался переход на /post,"
        f"но текущий URL: {driver.current_url}"
    )

    driver.back()
    sleep(1)

    print("\n[УСПЕХ] Тест успешно выполнен!")
