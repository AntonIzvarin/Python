import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    safari_driver = webdriver.Safari()
    safari_driver.maximize_window()
    yield safari_driver
    safari_driver.quit()


@allure.feature("Оформление заказа в магазине")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title(
    "Сквозной сценарий покупки товаров и проверка итогового чека")
@allure.description(
    "Тест проверяет авторизацию пользователя, "
    "добавление нескольких позиций "
    "товаров в корзину, заполнение контактной формы "
    "и финальный расчет общей суммы заказа."
)
def test_shopping_flow(driver: WebDriver) -> None:
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login(
        username="standard_user", password="secret_sauce"
    )

    inventory_page.add_item_to_cart("sauce-labs-backpack")
    inventory_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
    inventory_page.add_item_to_cart("sauce-labs-onesie")
    inventory_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.fill_checkout_form(
        first_name="Ivan",
        last_name="Petrov",
        zip_code="123456"
    )
    checkout_page.click_continue()

    total_text = checkout_page.get_total_price_text()

    with allure.step(
            "Проверка наличия итоговой суммы '$58.29' на странице расчета"
    ):
        assert (
            "$58.29" in total_text
        ), f"Ожидалась сумма $58.29, но на странице: '{total_text}'"
