import time
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

# pytest -s -v --language=es
# pytest -s -v --browser_name=firefox
# pytest -s -v --language=es --browser_name=firefox
