import time

from conftest import take_screenshot
from pages.help_page import HelpPage


def test_help(auth):
    help_page = HelpPage(auth)
    help_page.navigate_to_test_case_creation()
    help_page.scroll_to_header()
    help_page.highlight_header()
    take_screenshot(auth, "step_2_help")
