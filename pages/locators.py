from selenium.webdriver.common.by import By

#class MainPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")
     
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_TITLE_IN_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) .alertinner > strong")
    BOOK_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(3) .alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")

class DeleteProfilePageLocators():
        PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
        DELETE_BUTTON =  (By.CSS_SELECTOR, "button.btn-danger[type='submit']")
