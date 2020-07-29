from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_books_in_basket(self):
        assert self.element_not_present(*BasketPageLocators.BASKET_FORMSET), "Book present in the basket"

    def empty_basket_page_text_present(self):
        basket_empty_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        assert "Your basket is empty." in basket_empty_text, "Empty basket page text is not present"