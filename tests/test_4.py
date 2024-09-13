from conftest import take_screenshot
from pages.base_func_page import BaseFuncPage


def test_base_func(auth):
    base_func_page = BaseFuncPage(auth)
    base_func_page.navigate_to_base_func()
    base_func_page.navigate_to_use_func()
    base_func_page.navigate_to_ssh_func()
    take_screenshot(auth, "step_5_basefunc")
