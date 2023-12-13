import time
import pytest

from .pages.locators import Endpoints
from .pages.book_page_promo import BookPagePromo


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
    page = BookPagePromo(browser, link)  # initialization an instance
    page.open()  # already added into BasePage
    page.add_book_to_basket()
    page.solve_quiz_and_get_code()  # already added into BasePage
    page.book_should_be_added_to_card()
    page.price_should_be_correct()

# pytest -s test_foo.py
