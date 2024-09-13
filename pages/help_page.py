from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HelpPage(BasePage):
    HELP_MENU = (By.CSS_SELECTOR, '#aside > div > div.flex.scrollable.hover > div > ul.nav.bg > li:nth-child(2) > a')
    CREATE_TEST_CASE = (
        By.XPATH, '//a[@rel="link" and contains(@class, "vsb-nav-link") and text()=" Создание описания тест-кейса "]')
    HEADER_H3 = (By.XPATH, "//li[text()='Заголовок H3']")
    LOADER = (By.XPATH, '//*[@id="loader-default"]')
    ENTER_TITLE = (By.XPATH, '//*[@id="введение"]')

    def navigate_to_test_case_creation(self) -> None:
        self.click_element(self.HELP_MENU)
        self.find_visibility_element(self.ENTER_TITLE)
        self.click_element(self.CREATE_TEST_CASE)

    def scroll_to_header(self) -> None:
        sleep(1)  # Ждем полную загрузку страницы
        element = self.find_presence_element(self.HEADER_H3)
        self.scroll_to_element(element)

    def highlight_header(self) -> None:
        element = self.find_presence_element(self.HEADER_H3)
        self.highlight_element(element)
