from selenium.common import NoSuchElementException

from .base_page import BasePage
from .locators import BookPageLocators


class BookPagePromo(BasePage):

    def add_book_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*BookPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def book_should_be_added_to_card(self):
        book_name_form_alert = self.browser.find_element(*BookPageLocators.BOOK_NAME_FROM_ALERT)
        book_name_form_page = self.browser.find_element(*BookPageLocators.BOOK_NAME_FROM_PAGE)
        try:
            assert book_name_form_alert.text == book_name_form_page.text, "book names not match!"
        except NoSuchElementException:
            assert False, "book name not found!"

    def price_should_be_correct(self):
        price_book_from_alert = self.browser.find_element(*BookPageLocators.AMOUNT_FROM_ALERT)
        price_book_from_page = self.browser.find_element(*BookPageLocators.BOOK_PRICE)
        try:
            assert price_book_from_alert.text == price_book_from_page.text, "prices not match!"
        except NoSuchElementException:
            assert False, "price not found!"
