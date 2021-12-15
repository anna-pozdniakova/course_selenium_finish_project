from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL_FIELD=(By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD1=(By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_FIELD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON=(By.CSS_SELECTOR, "button[value=Register]")

class AddProductLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    BOOK_NAME_ADDED = (By.CSS_SELECTOR, "#messages > :nth-child(1) > div > strong")
    BOOK_PRICE_ADDED = (By.CSS_SELECTOR, "#messages > :nth-child(3) > div > :nth-child(1) > strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK=(By.XPATH, "//a[contains(@href, 'basket')]")
    BASKET_ITEMS=(By.CSS_SELECTOR,"div.basket-items")
    BASKET_MESSAGE=(By.CSS_SELECTOR,"#content_inner > p > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
