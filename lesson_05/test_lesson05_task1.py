from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    # 1. Открываем главную страницу
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")
    sleep(3)

    # 2. Кликаем по ссылке формы
    css_sel = "[href='/forms/post']"
    html_from_click = driver.find_element(By.CSS_SELECTOR, css_sel)
    html_from_click.click()
    sleep(1)

    # Проверяем, что перешли на страницу формы
    assert "/forms/post" in driver.current_url, (
        f"Ошибка! Ожидался переход на /forms/post, "
        f"но текущий URL: {driver.current_url}"
    )

    # 3. Возвращаемся назад
    driver.back()
    sleep(1)

    # Проверяем, что вернулись на главную страницу
    assert driver.current_url == "https://httpbin.qa-territory.online/", (
        f"Ошибка! Браузер не вернулся на главную страницу. "
        f"Текущий URL: {driver.current_url}"
    )

    # 4. Выводим сообщение об успехе в консоль
    print("\n[УСПЕХ] Тест успешно выполнен!")
