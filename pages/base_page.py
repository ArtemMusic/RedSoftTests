from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)

    def find_visibility_element(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_invisibility_element(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(
            EC.invisibility_of_element(locator)
        )

    def find_presence_element(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator: tuple[str, str]) -> None:
        self.find_visibility_element(locator)
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def wait_invisibility_element(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    def scroll_to_element(self, element: WebElement) -> WebElement:
        return self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def highlight_element(self, element: WebElement) -> WebElement:
        return self.browser.execute_script("arguments[0].style.backgroundColor = 'yellow';", element)

    def find_elements_with_wait(self, locator: tuple[str, str]) -> list[WebElement]:
        self.find_presence_element(locator)
        by_type, by_text = locator
        return self.browser.find_elements(by_type, by_text)
