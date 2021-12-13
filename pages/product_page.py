from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import AddProductLocators
import math

class ProductPage(BasePage):
    def add_product(self):
        button_add = self.browser.find_element(*AddProductLocators.ADD_BUTTON)
        button_add.click()

    def should_be_message_add_basket(self):
        self.add_product()
        assert self.solve_quiz_and_get_code(), "No second alert presented"

    def should_be_message_by_book_name(self):
        #assert self.is_element_present(*AddProductLocators.BOOK_NAME), "not be name1"
        text1 = self.browser.find_element(*AddProductLocators.BOOK_NAME).text
        self.add_product()
        self.solve_quiz_and_get_code()
        el2 = self.browser.find_element(*AddProductLocators.BOOK_NAME_ADDED)
        #assert self.is_element_present(*AddProductLocators.BOOK_NAME_ADDED), "not be name"
        assert text1==el2.text, "Another name"

    def should_be_message_by_price(self):
        price1 = self.browser.find_element(*AddProductLocators.BOOK_PRICE).text
        self.add_product()
        self.solve_quiz_and_get_code()
        el2 = self.browser.find_element(*AddProductLocators.BOOK_PRICE_ADDED)
        assert price1 == el2.text, "Another price"
        #assert self.is_element_present(*AddProductLocators.BOOK_PRICE_ADDED), "Not be price"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            return True
        except NoAlertPresentException:
            return False
            #print("No second alert presented")
