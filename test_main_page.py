import time
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()



# pytest -s -v --language=es
# pytest -s -v --browser_name=firefox
# pytest -s -v --language=es --browser_name=firefox
# pytest -v --tb=line --language=en test_main_page.py

