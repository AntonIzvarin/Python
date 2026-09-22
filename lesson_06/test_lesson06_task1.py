from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_dynamic_loading():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        submit_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        submit_button.click()

        wait = WebDriverWait(driver, 10)
        finish_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        driver.save_screenshot("screenshot_task1.png")

        err = f"Ожидался 'Hello World!', но получен '{finish_element.text}'"
        assert finish_element.text == "Hello World!", err

    finally:

        driver.quit()
