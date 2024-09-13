from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='ldap_username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='ldap_password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary.mb-4")

    def login(self, username: str, password: str) -> None:
        self.find_visibility_element(self.USERNAME_INPUT).send_keys(username)
        self.find_visibility_element(self.PASSWORD_INPUT).send_keys(password)
        self.click_element(self.LOGIN_BUTTON)
