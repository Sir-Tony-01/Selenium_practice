from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_full_order_flow(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    assert inventory.is_loaded()

    inventory.add_first_item_to_cart()
    assert inventory.get_cart_count() == "1", "Item not added to cart"

    inventory.go_to_cart()

    cart = CartPage(logged_in_driver)
    cart.click_checkout()

    checkout = CheckoutPage(logged_in_driver)
    checkout.fill_checkout_info("Test", "User", "12345")
    checkout.continue_checkout()
    checkout.finish_checkout()
    assert checkout.is_checkout_complete(), "Checkout not completed"
