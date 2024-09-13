from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class DarkmodePage(BasePage):
    SETTINGS_BUTTON = (By.XPATH, '//*[@id="accountInfo"]/div/ul/li[3]/a')
    SWITCH_MODE = (By.XPATH, "//*[@class='radio radio-inline ui-check ui-check-color ui-check-md']")
    ALERT_CLOSE = (By.XPATH, '//*[@id="alert"]/button')

    def setting_button_click(self) -> WebElement | None:
        try:
            return self.click_element(self.SETTINGS_BUTTON)
        except (TimeoutException, ElementClickInterceptedException):
            self.click_element(self.ALERT_CLOSE)
            self.wait_invisibility_element(self.ALERT_CLOSE)
            self.click_element(self.SETTINGS_BUTTON)

    def switch_mode_click(self) -> None:
        self.click_element(self.SWITCH_MODE)
