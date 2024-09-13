from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CasePage(BasePage):
    CASE_TAB = (By.XPATH, "//span[text()='Кейс']")
    LIST_TAB = (By.XPATH, "//span[text()='Список']")
    SUB_LIST = (By.TAG_NAME, 'a')
    PROJECT_BUTTON = (By.XPATH, '//*[@id="dragLeft"]/div[1]/div/div[1]/div/button')
    PROJECT_MENU = (By.CSS_SELECTOR, '//*[@id="dragLeft"]/div[1]/div/div[1]/div/div')
    VERSION_BUTTON = (By.XPATH, '//*[@id="dragLeft"]/div[1]/div/div[2]/div/button')
    VERSION_MENU = (By.CSS_SELECTOR, '//*[@id="dragLeft"]/div[1]/div/div[2]/div/div')
    LOADER = (By.XPATH, '//*[@id="loader-default"]')

    def select_project_list(self) -> None:
        self.click_element(self.CASE_TAB)
        self.click_element(self.LIST_TAB)

    def select_project(self, project_name: str, project_ver: str) -> None:
        project_title = self.find_visibility_element(self.PROJECT_BUTTON).text.strip().lower()

        if project_title != project_name.strip().lower():
            self.click_element(self.PROJECT_BUTTON)
            self.find_visibility_element(self.PROJECT_MENU)
            project_links = self.find_elements_with_wait(self.SUB_LIST)

            for project_link in project_links:
                if project_link.text.strip().lower() == project_name.strip().lower():
                    project_link.click()
                    break

        project_version = self.find_visibility_element(self.VERSION_BUTTON).text.strip().lower()

        if project_version != project_ver.strip().lower():
            self.click_element(self.VERSION_BUTTON)
            self.find_visibility_element(self.VERSION_MENU)
            version_links = self.find_elements_with_wait(self.SUB_LIST)

            for version_link in version_links:
                if version_link.text.strip() == project_ver.strip().lower():
                    version_link.click()
                    break
