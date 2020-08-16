from .base_page import BasePage
from .locators import DeleteProfilePageLocators

class DeleteProfilePage(BasePage):
    def delete_user(self, password):
        self.browser.find_element(*DeleteProfilePageLocators.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*DeleteProfilePageLocators.DELETE_BUTTON).click()