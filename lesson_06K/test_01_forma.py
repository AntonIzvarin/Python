from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    # 1. Инициализируем драйвер
    driver = webdriver.Safari()
    driver.maximize_window()

    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    # Создаем объект явного ожидания на 10 секунд
    wait = WebDriverWait(driver, 10)

    # 2. Безопасно ожидаем появление каждого поля и заполняем форму
    wait.until(
        EC.presence_of_element_located((By.NAME, "first-name")),
        "Не найдено поле first-name",
    ).send_keys("Иван")

    wait.until(
        EC.presence_of_element_located((By.NAME, "last-name")),
        "Не найдено поле last-name",
    ).send_keys("Петров")

    wait.until(
        EC.presence_of_element_located((By.NAME, "address")),
        "Не найдено поле address",
    ).send_keys("Ленина, 55-3")

    wait.until(
        EC.presence_of_element_located((By.NAME, "e-mail")),
        "Не найдено поле e-mail",
    ).send_keys("test@skypro.com")

    wait.until(
        EC.presence_of_element_located((By.NAME, "phone")),
        "Не найдено поле phone",
    ).send_keys("+7985899998787")

    # Zip code оставляем пустым
    zip_field = wait.until(
        EC.presence_of_element_located((By.NAME, "zip-code")),
        "Не найдено поле zip-code",
    )
    zip_field.clear()

    wait.until(
        EC.presence_of_element_located((By.NAME, "city")),
        "Не найдено поле city"
    ).send_keys("Москва")

    wait.until(
        EC.presence_of_element_located((By.NAME, "country")),
        "Не найдено поле country",
    ).send_keys("Россия")

    wait.until(
        EC.presence_of_element_located((By.NAME, "job-position")),
        "Не найдено поле job-position",
    ).send_keys("QA")

    wait.until(
        EC.presence_of_element_located((By.NAME, "company")),
        "Не найдено поле company",
    ).send_keys("SkyPro")

    # 3. Находим кнопку Submit через ожидание и кликаем
    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")),
        "Кнопка Submit некликабельна",
    )
    submit_button.click()

    # 4. Ожидаем валидации формы
    wait.until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, "#zip-code.alert-danger"
        )),
        "Форма не отвалидировалась: поле Zip-code не стало красным",
    )

    # 5. ПРОВЕРКИ (Asserts)
    zip_field_after = driver.find_element(By.ID, "zip-code")
    assert (
            "alert-danger" in zip_field_after.get_attribute("class")
    ), "Поле Zip code не подсвечено красным!"

    # Список ID полей, которые должны стать зелеными
    green_fields_ids = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company",
    ]

    for field_id in green_fields_ids:
        field = driver.find_element(By.ID, field_id)
        assert (
                "alert-success" in field.get_attribute("class")
        ), f"Поле {field_id} не подсвечено зеленым!"

    # Закрываем сессию
    driver.quit()
