from conftest import take_screenshot
from pages.case_in_develop_page import CaseInDevelop


def test_case_in_develop(auth):
    case_in_develop = CaseInDevelop(auth)
    case_in_develop.switch_in_develop()
    case_in_develop.switch_in_auto()
    case_in_develop.add_tracker_link("https://185.61.26.174/ru/case/list/?filter=&prarch=2&id=30&panel=0")
    take_screenshot(auth, "step_6_indevelop")
