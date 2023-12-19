from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BookPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    AMOUNT_FROM_ALERT = (By.CSS_SELECTOR, ".alertinner p strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BOOK_NAME_FROM_ALERT = (By.CSS_SELECTOR, ".alert-safe:first-child > div.alertinner > strong")
    BOOK_NAME_FROM_PAGE = (By.CSS_SELECTOR, ".product_main > h1")


class Endpoints:
    BASIC_URL = 'http://selenium1py.pythonanywhere.com/'
    LOGIN_PAGE_ENDPOINT = 'accounts/login/'
    BOOK_PAGE_ENDPOINT_PROMO = 'catalogue/the-shellcoders-handbook_209/?promo=newYear'
    BOOK_PAGE_ENDPOINT_PROMO_207 = 'catalogue/coders-at-work_207/?promo=newYear2019'
    URL_CODERS_AT_WORK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    BOOK_PAGE_ENDPOINT = "catalogue/the-shellcoders-handbook_209"
    BOOK_CITY_AND_STARS = "catalogue/the-city-and-the-stars_95/"
