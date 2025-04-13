from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_order_flow(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded(), "Login failed: Inventory page not loaded"
