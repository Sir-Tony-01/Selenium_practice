from pages.login_page import LoginPage

def test_locked_out_user_cannot_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    error_message = login_page.get_error_message()
    assert "locked out" in error_message.lower(), f"Unexpected error: {error_message}"