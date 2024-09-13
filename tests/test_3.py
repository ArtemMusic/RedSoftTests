from conftest import take_screenshot
from pages.case_page import CasePage


def test_case(auth):
    case_page = CasePage(auth)
    case_page.select_project_list()
    case_page.select_project('РЕД АДМ', '1.9.1')
    take_screenshot(auth, "step_4_case")
