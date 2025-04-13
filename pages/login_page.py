
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element("xpath", "//input[@data-test='username']").send_keys(username)
        self.driver.find_element("xpath", "//input[@data-test='password']").send_keys(password)
        self.driver.find_element("xpath", "//input[@data-test='login-button']").click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(("class name", "error-message-container"))
        ).text
