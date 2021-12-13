from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class AddProductLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    BOOK_NAME_ADDED = (By.CSS_SELECTOR, "#messages > :nth-child(1) > div > strong")
    BOOK_PRICE_ADDED = (By.CSS_SELECTOR, "#messages > :nth-child(3) > div > :nth-child(1) > strong")
