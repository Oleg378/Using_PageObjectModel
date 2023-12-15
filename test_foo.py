import time
import pytest

from .pages.locators import Endpoints
from .pages.book_page_promo import BookPage


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
def test_user_can_add_book_to_basket(browser, test_link):
    link = f"{test_link}"
    # link = Endpoints.BASIC_URL + Endpoints.BOOK_PAGE_ENDPOINT_PROMO_207
    page = BookPage(browser, link)  # initialization an instance
    page.open()  # already added into BasePage
    page.add_book_to_basket()
    page.solve_quiz_and_get_code()  # already added into BasePage
    page.book_should_be_added_to_card()
    page.price_should_be_correct()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = Endpoints.BASIC_URL + Endpoints.BOOK_PAGE_ENDPOINT
    page = BookPage(browser, link)
    page.open()
    page.add_book_to_basket()
    page.should_not_be_success_message()  # negative test via .is_not_element_present()


def test_guest_cant_see_success_message(browser):
    link = Endpoints.BASIC_URL + Endpoints.BOOK_PAGE_ENDPOINT
    page = BookPage(browser, link)
    page.open()
    page.should_not_be_success_message()  # positive test via .is_not_element_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = Endpoints.BASIC_URL + Endpoints.BOOK_PAGE_ENDPOINT
    page = BookPage(browser, link)
    page.open()
    page.add_book_to_basket()
    page.should_disappear_success_message()  # negative test via .is_disappeared()

# pytest -s test_foo.py
