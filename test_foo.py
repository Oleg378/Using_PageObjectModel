import time

from .pages.locators import Endpoints
from .pages.book_page_promo import BookPagePromo


def test_user_can_add_book_to_basket(browser):
    link = Endpoints.BASIC_URL + Endpoints.BOOK_PAGE_ENDPOINT_PROMO_207
    page = BookPagePromo(browser, link)  # initialization an instance
    page.open()  # already added into BasePage
    page.add_book_to_basket()
    page.solve_quiz_and_get_code()  # already added into BasePage
    page.book_should_be_added_to_card()
    page.price_should_be_correct()

# pytest -s test_foo.py
