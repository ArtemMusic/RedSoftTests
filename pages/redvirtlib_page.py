from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RedvirtlibPage(BasePage):
    LIB_PAGE = (By.XPATH, "//a[text()=' Библиотека redvirtlib ']")
    LANGUAGE_PY = (By.CLASS_NAME, 'language-py')

    def navigate_to_redvirtlib(self) -> None:
        self.click_element(self.LIB_PAGE)

    def highlight_elements(self) -> None:
        elements = self.find_elements_with_wait(self.LANGUAGE_PY)
        for element in elements:
            self.scroll_to_element(element)
            self.highlight_element(element)
