from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class CaseInDevelop(BasePage):
    TRACKER_BUTTON = (By.XPATH, '//*[@id="info"]/div/div[1]/div[11]/div[2]/div/div/a')
    TRACKER_INPUT = (By.XPATH, '//*[@id="addTrackerURLInput"]')
    STATUS = (By.XPATH, '//*[@id="info"]/div/div[1]/div[1]/div[2]/span/span')
    ADD_BUTTON = (By.XPATH, '//*[@id="info"]/div/div[1]/div[11]/div[2]/div/div/div/div/div/button[2]')
    LOADER = (By.XPATH, '//*[@id="loader-default"]')

    IN_DEVELOP_LABEL = (By.CSS_SELECTOR, 'div.pb-2:nth-child(2) > div:nth-child(2) > label:nth-child(1)')
    IN_DEVELOP_INPUT = (
        By.CSS_SELECTOR, 'div.pb-2:nth-child(2) > div:nth-child(2) > label:nth-child(1) > input:nth-child(1)')
    AUTO_INPUT = (By.CSS_SELECTOR, 'div.pb-2:nth-child(3) > div:nth-child(2) > label:nth-child(1) > input:nth-child(1)')
    AUTO_LABEL = (By.CSS_SELECTOR, 'div.pb-2:nth-child(3) > div:nth-child(2) > label:nth-child(1)')

    def _switch_checkbox(self, checkbox: tuple[str, str], label: tuple[str, str]) -> WebElement | None:
        self.find_invisibility_element(self.LOADER)
        if self.find_presence_element(checkbox).get_attribute('checked') is None:
            return self.click_element(label)

    def switch_in_develop(self) -> WebElement:
        self.find_elements_with_wait(self.IN_DEVELOP_LABEL)
        return self._switch_checkbox(self.IN_DEVELOP_INPUT, self.IN_DEVELOP_LABEL)

    def switch_in_auto(self) -> WebElement:
        return self._switch_checkbox(self.AUTO_INPUT, self.AUTO_LABEL)

    def add_tracker_link(self, link: str) -> None:
        try:
            if self.find_presence_element(self.STATUS).text.strip().lower() == "подготовка":
                self.wait_invisibility_element(self.LOADER)
                self.click_element(self.TRACKER_BUTTON)
                self.find_visibility_element(self.TRACKER_INPUT).send_keys(link)
                self.click_element(self.ADD_BUTTON)
        except TimeoutException:
            print('Ссылка на трекер была вставлена ранее')
