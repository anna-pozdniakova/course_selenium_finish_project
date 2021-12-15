from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import time
import pytest

link_main_page = "http://selenium1py.pythonanywhere.com/"
link_product = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link_main_page)
        page.open()
        page.go_to_login_page()
        #login_page = LoginPage(browser, browser.current_url)
        #login_page.should_be_login_page()

    @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link_main_page)
        page.open()
        page.should_be_login_link()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.should_be_click_login()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link_main_page)
    page.open()
    page.open_basket()
    page.should_not_be_product_in_basket()
    page.should_not_be_message_empty_in_basket()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link_product)
    page.open()
    page.open_basket()
    page.should_not_be_product_in_basket()
    page.should_not_be_message_empty_in_basket()



