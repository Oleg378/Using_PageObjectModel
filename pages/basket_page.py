from .base_page import BasePage
from .locators import BasketPageLocators, Endpoints


class BasketPage(BasePage):
    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ALL_BASKET_ITEMS), \
            "list of goods is not empty, but should be"

    def should_be_empty_message(self):
        assert len(self.browser.find_elements(*BasketPageLocators.EMPTY_BASKET_MESSAGE)) == 1, \
            "There is no empty message, but should be"
