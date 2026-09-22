from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._checkout_button = (By.CSS_SELECTOR, "#checkout")

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self._checkout_button)
        ).click()
