import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import Endpoints


def test_guest_can_go_to_login_page(browser):
    link = Endpoints.BASIC_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = Endpoints.BASIC_URL
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = Endpoints.BASIC_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_goods_in_basket()
    basket_page.should_be_empty_message()


# pytest -s -v --language=es
# pytest -s -v --browser_name=firefox
# pytest -s -v --language=es --browser_name=firefox
# pytest -v --tb=line --language=en test_main_page.py
