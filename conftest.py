import os
from time import sleep

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage

load_dotenv()

screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
os.makedirs(screenshot_dir, exist_ok=True)


@pytest.fixture(scope="session")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def auth(browser):
    browser.get(str(os.getenv("BASE_URL")))
    login_page = LoginPage(browser)
    login_page.login(str(os.getenv("LOGIN_USER")), str(os.getenv("LOGIN_PASS")))
    take_screenshot(browser, "step_1_auth")
    yield browser


def take_screenshot(driver, name):
    sleep(2) # Чтобы корректно сделать скриншот
    path = os.path.join(screenshot_dir, f"{name}.png")
    driver.save_screenshot(path)
