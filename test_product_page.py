from .pages.product_page import ProductPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_message_add_basket()

def test_correct_name(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_message_by_book_name()

def test_correct_price(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_message_by_price()


