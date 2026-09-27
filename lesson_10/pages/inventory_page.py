import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)
        self._shopping_cart_link: tuple[str, str] = (
            By.CSS_SELECTOR, ".shopping_cart_link")

    @allure.step("Добавить товар '{item_id_name}' в корзину")
    def add_item_to_cart(self, item_id_name: str) -> None:
        """
        Находит кнопку добавления конкретного товара и кликает на нее.
        """
        locator = (By.CSS_SELECTOR, f"#add-to-cart-{item_id_name}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Перейти в корзину покупок")
    def go_to_cart(self) -> None:
        """
        Выполняет переход на страницу просмотра корзины.
        """
        self.wait.until(
            EC.element_to_be_clickable(self._shopping_cart_link)
        ).click()
