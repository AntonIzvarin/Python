from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://gitflic.ru/")
    # Добавляем cookie с токеном авторизации
    driver.add_cookie(
        {
            "name": "SESSION",
            "value": "MWNhZmRmOTUtNDg4Ni00YWY2LThhOTItMmFhYWJlMjMzYTcx",
            "domain": "gitflic.ru",
        }
    )
    # Добавляем cookie для окна подтверждения работы с cookie
    driver.add_cookie(
        {"name": "cookiesAccepted", "value": "true", "domain": "gitflic.ru"}
    )
    # Обновляем страницу, чтобы cookie применилась
    driver.refresh()
    # Теперь мы авторизованы!
    # Можем сразу перейти в личный кабинет
    driver.get("https://gitflic.ru/user/anton180188")

    wait.until(EC.url_contains("anton180188"))

    url_1 = driver.current_url
    # Удаляем все cookies (выходим из аккаунта)
    driver.delete_all_cookies()
    # Обновляем страницу
    driver.refresh()

    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    # Добавляем cookie с токеном авторизации
    driver.add_cookie(
        {
            "name": "SESSION",
            "value": "ZGZiNWYxMGEtYTE2My00ZGY4LWIwOGYtNWVmYzdkMGVhNzMy",
            "domain": "gitflic.ru",
        }
    )
    # Добавляем cookie для окна подтверждения работы с cookie
    driver.add_cookie(
        {"name": "cookiesAccepted", "value": "true", "domain": "gitflic.ru"}
    )
    # Обновляем страницу, чтобы cookie применилась
    driver.refresh()
    # Теперь мы авторизованы!
    # Можем сразу перейти в личный кабинет
    driver.get("https://gitflic.ru/user/qwerty180188")

    wait.until(EC.url_contains("qwerty180188"))

    url_2 = driver.current_url
    # Удаляем все cookies (выходим из аккаунта)
    driver.delete_all_cookies()
    # Обновляем страницу
    driver.refresh()

    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    assert url_1 != url_2, f"Ожидалось, что URL будут разными, но оба равны: {url_1}"

    driver.quit()
