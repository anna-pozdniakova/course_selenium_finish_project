from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def open_basket(self):
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), \
            "List products is presented, but should not be"

    def should_not_be_message_empty_in_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_MESSAGE), \
            "Empty basket message be not, but should not be"