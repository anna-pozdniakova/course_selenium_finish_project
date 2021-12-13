from .pages.product_page import ProductPage
import time
import pytest

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

@pytest.mark.parametrize('ind', range(0,10))
def test_correct_name(browser,ind):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{ind}'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_message_by_book_name()

def test_correct_price(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_message_by_price()



