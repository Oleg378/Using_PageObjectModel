import time
import pytest
import random

from .pages.locators import Endpoints
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.parametrize('test_link', [Endpoints.URL_CODERS_AT_WORK + "?promo=offer0",
                                       # Endpoints.URL_CODERS_AT_WORK + "?promo=offer1",
                                       # Endpoints.URL_CODERS_AT_WORK + "?promo=offer2",
                                       # Endpoints.URL_CODERS_AT_WORK + "?promo=offer3",
                                       # Endpoints.URL_CODERS_AT_WORK + "?promo=offer4",
                                       # Endpoints.URL_CODERS_AT_WORK + "?promo=offer5",
                                       Endpoints.URL_CODERS_AT_WORK + "?promo=offer6",
                                       pytest.param(Endpoints.URL_CODERS_AT_WORK + "?promo=offer7",
                                                    marks=pytest.mark.xfail),
                                       Endpoints.URL_CODERS_AT_WORK + "?promo=offer8",
                                       Endpoints.URL_CODERS_AT_WORK + "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, test_link):
    link = f"{test_link}"
    # link = Endpoints.BASIC_URL + Endpoints.BOOK_PAGE_ENDPOINT_PROMO_207
    page = ProductPage(browser, link)  # initialization an instance
    page.open()  # already added into BasePage
    page.add_book_to_basket()
    page.solve_quiz_and_get_code()  # already added into BasePage
    page.book_should_be_added_to_card()
    page.price_should_be_correct()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = Endpoints.BASIC_URL + Endpoints.BOOK_PAGE_ENDPOINT
    page = ProductPage(browser, link)
    page.open()
    page.add_book_to_basket()
    page.should_not_be_success_message()  # negative test via .is_not_element_present()


def test_guest_cant_see_success_message(browser):
    link = Endpoints.BASIC_URL + Endpoints.BOOK_PAGE_ENDPOINT
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()  # positive test via .is_not_element_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = Endpoints.BASIC_URL + Endpoints.BOOK_PAGE_ENDPOINT
    page = ProductPage(browser, link)
    page.open()
    page.add_book_to_basket()
    page.should_disappear_success_message()  # negative test via .is_disappeared()


@pytest.mark.registered_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = Endpoints.BASIC_URL + Endpoints.LOGIN_PAGE_ENDPOINT
        page = LoginPage(browser, link)
        page.open()
        email = str(random.randint(1000, 9999)) + "@example.com"
        password = str(random.randint(1000000000, 99999999999))
        page.register_new_user(email, password)
        page.should_be_authorized_user()

        yield
        page.logout()

    def test_user_cant_see_success_message(self, browser):
        link = Endpoints.BASIC_URL + Endpoints.BOOK_PAGE_ENDPOINT
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()  # positive test via .is_not_element_present()

    def test_user_can_add_product_to_basket(self, browser):
        link = Endpoints.BASIC_URL + Endpoints.BOOK_PAGE_ENDPOINT
        page = ProductPage(browser, link)  # initialization an instance
        page.open()  # already added into BasePage
        page.add_book_to_basket()
        page.book_should_be_added_to_card()
        page.price_should_be_correct()


def test_guest_should_see_login_link_on_product_page(browser):
    link = Endpoints.BASIC_URL + Endpoints.BOOK_CITY_AND_STARS
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = Endpoints.BASIC_URL + Endpoints.BOOK_CITY_AND_STARS
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = Endpoints.BASIC_URL + Endpoints.BOOK_CITY_AND_STARS
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_goods_in_basket()
    basket_page.should_be_empty_message()

# pytest -s test_product_page.py
# pytest -v -s test_product_page.py::test_guest_cant_see_product_in_basket_opened_from_product_page
# pytest -m registered_user

