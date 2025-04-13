


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return self.driver.find_element("class name", "inventory_list").is_displayed()

    def add_first_item_to_cart(self):
        self.driver.find_element("xpath", "(//button[contains(@id, 'add-to-cart')])[1]").click()

    def go_to_cart(self):
        self.driver.find_element("class name", "shopping_cart_link").click()

    def get_cart_count(self):
        try:
            return self.driver.find_element("class name", "shopping_cart_badge").text
        except:
            return "0"

