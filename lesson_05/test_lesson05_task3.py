from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# 1. Открываем страницу https://httpbin.qa-territory.online/links/10
def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")
    sleep(3)

    # 2. Находим все ссылки на странице (тег <a>)
    links = driver.find_elements(By.TAG_NAME, "a")

    # 3. Проверяем с помощью len(), что количество ссылок равно 9
    links_count = len(links)
    assert (
        links_count == 9
    ), f"Ошибка! Ожидалось 9 ссылок, но len() вернул: {links_count}"
    sleep(3)

    # 4. Используем цикл для проверки отображения каждого элемента
    for link in links:
        assert (
            link.is_displayed()
        ), "Ошибка! Одна из ссылок не отображается на странице."

    # 5. Для проверки первой ссылки используем индекс [0]
    first_link_text = links[0].text
    assert (
        "1" in first_link_text
    ), f"Ошибка! Текст первой ссылки ('{first_link_text}') не содержит '1'"
    print(f"[УСПЕХ] Текст первой ссылки ('{first_link_text}') содержит '1'.")

    print("\n[ФИНАЛ] Все проверки успешно пройдены!")

    driver.quit()
