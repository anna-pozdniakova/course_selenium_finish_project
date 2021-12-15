from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import AddProductLocators
from .locators import MainPageLocators
from .locators import BasePageLocators
import math

class ProductPage(BasePage):
    def add_product(self):
        button_add = self.browser.find_element(*AddProductLocators.ADD_BUTTON)
        button_add.click()

    def should_be_message_add_basket(self):
        self.add_product()
        assert self.solve_quiz_and_get_code(), "No second alert presented"

    def should_be_message_by_book_name(self, check=True):
        text1 = self.browser.find_element(*AddProductLocators.BOOK_NAME).text
        self.add_product()
        if check:
            self.solve_quiz_and_get_code()
        el2 = self.browser.find_element(*AddProductLocators.BOOK_NAME_ADDED)
        assert text1==el2.text, f"Another name: '{text1}' and '{el2.text}'"

    def should_be_message_by_price(self, check=True):
        price1 = self.browser.find_element(*AddProductLocators.BOOK_PRICE).text
        self.add_product()
        if check:
            self.solve_quiz_and_get_code()
        el2 = self.browser.find_element(*AddProductLocators.BOOK_PRICE_ADDED)
        assert price1 == el2.text, f"Another price: '{price1}' and '{el2.text}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*AddProductLocators.BOOK_NAME_ADDED), \
            "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*AddProductLocators.BOOK_NAME_ADDED), \
            "Success message is disappeared, but should be"

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
        except NoAlertPresentException:
            print("No second alert")

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "URL not considered 'login'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def should_be_click_login(self):
        assert self.is_clicked(*MainPageLocators.LOGIN_LINK), "Not clickable login link"


