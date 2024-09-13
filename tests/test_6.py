from conftest import take_screenshot
from pages.darkmode_page import DarkmodePage


def test_darkmode(auth):
    darkmode = DarkmodePage(auth)
    darkmode.setting_button_click()
    darkmode.switch_mode_click()
    take_screenshot(auth, "step_7_darkmode")
