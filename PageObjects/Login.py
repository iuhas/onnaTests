import time


class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    user_email = "qateam.onna@destinoalgum.com.br"
    user_password = "Onna12345678!"

    def login(self):
        login_username = self.browser.find_element_by_id('username-input')
        login_username.click()
        login_username.send_keys(self.user_email)

        login_password = self.browser.find_element_by_id("userpass-input")
        login_password.send_keys(self.user_password)
        login_button = self.browser.find_element_by_css_selector(".pa-button-label")
        login_button.click()
        time.sleep(8)