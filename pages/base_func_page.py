from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BaseFuncPage(BasePage):
    BASE_FUNC = (By.XPATH, "//*[@id='caseGroupNav1']")
    USE = (By.XPATH, "//*[@id='caseSubGroupNav3']")
    SSH_KEYGEN = (By.XPATH, "//*[@id='navSubGroup3']")

    def navigate_to_base_func(self):
        self.click_element(self.BASE_FUNC)

    def navigate_to_use_func(self):
        self.click_element(self.USE)

    def navigate_to_ssh_func(self):
        self.click_element(self.SSH_KEYGEN)
