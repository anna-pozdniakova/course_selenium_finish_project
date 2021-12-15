from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest

link_promo_2019 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
link_main_page = "http://selenium1py.pythonanywhere.com/"
link_product = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

class TestGuestAddToBasketFromProductPage:
    @pytest.mark.parametrize('ind', range(0,10))
    def test_correct_name(self, browser,ind):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{ind}'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_message_by_book_name()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_promo_2019)
        page.open()
        page.should_be_message_by_book_name()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link_product)
        page.open()
        page.should_be_click_login()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = BasketPage(browser, link_main_page)
        page.open()
        page.open_basket()
        page.should_not_be_product_in_basket()
        page.should_not_be_message_empty_in_basket()

    def test_correct_price(self, browser):
        page = ProductPage(browser, link_promo_2019)
        page.open()
        page.should_be_message_by_price()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link_promo_2019)
        page.open()
        page.add_product()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_promo_2019)
        page.open()
        page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link_promo_2019)
        page.open()
        page.add_product()
        page.solve_quiz_and_get_code()
        page.should_be_disappeared_message()

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link_main_page)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, '12_Rfgtj-f89')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_product)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_product)
        page.open()
        page.should_be_message_by_book_name(False)
