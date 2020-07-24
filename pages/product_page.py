import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class ProductPage(BasePage):
    def add_book_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            WebDriverWait(self.browser, 1).until(expected_conditions.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except (NoAlertPresentException, TimeoutException):
            print("No second alert presented")

    def book_added_to_basket_message_appeared(self):
        self.book_name_in_message_equal_to_added_book()

    def book_name_in_message_equal_to_added_book(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        book_title_in_message = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_IN_MESSAGE).text

        assert book_title == book_title_in_message, "Book title doesn't match book title in message"

    def basket_cost_message_appeared(self):
        self.basket_cost_equal_to_book_price()

    def basket_cost_equal_to_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price_in_message = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_MESSAGE).text

        assert book_price == book_price_in_message, "Book price doesn't match book price in message"

    def success_message_not_present(self):
        
        assert self.element_not_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message present"

    def success_message_disappeared(self):
        
        assert self.element_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message not disappeared"