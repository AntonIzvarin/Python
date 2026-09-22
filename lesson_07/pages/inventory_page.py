from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._shopping_cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_item_to_cart(self, item_id_name: str):
        locator = (By.CSS_SELECTOR, f"#add-to-cart-{item_id_name}")
        # element_to_be_clickable обеспечивает готовность элемента к действию
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self._shopping_cart_link)
        ).click()
