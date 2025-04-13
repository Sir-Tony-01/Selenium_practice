
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_info(self, first_name, last_name, postal_code):

        self.driver.find_element("xpath", "//input[@id='first-name']").send_keys(first_name)
        self.driver.find_element("xpath", "//input[@id='last-name']").send_keys(last_name)
        self.driver.find_element("xpath", "//input[@id='postal-code']").send_keys(postal_code)

    def continue_checkout(self):
        self.driver.find_element("xpath", "//input[@id='continue']").click()

    def finish_checkout(self):
         WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(("xpath", "//button[@id='finish']"))
    ).click()

    def is_checkout_complete(self):
        return "Thank you for your order!" in self.driver.page_source
