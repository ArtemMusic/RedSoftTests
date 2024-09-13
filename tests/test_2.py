import time

from pages.redvirtlib_page import RedvirtlibPage


def test_redvirtlib(auth):
    redvirtlib_page = RedvirtlibPage(auth)
    redvirtlib_page.navigate_to_redvirtlib()
    redvirtlib_page.highlight_elements()
    time.sleep(0.5)  # Исключительно чтобы увидеть изменение фона. Не обязательно
