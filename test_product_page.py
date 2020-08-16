import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.delete_profile_page import DeleteProfilePage
import time

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user("asdfasdf@test.mail", "NX7fWt6MtVsJhXt")
        page.should_be_authorized_user()

        yield
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/profile/delete/"
        page = DeleteProfilePage(browser, link)
        page.open()
        page.delete_user("NX7fWt6MtVsJhXt")


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.success_message_not_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_book_to_basket()
        page.solve_quiz_and_get_code()
        time.sleep(5)
        page.book_added_to_basket_message_appeared()
        page.basket_cost_message_appeared()

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_book_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.book_added_to_basket_message_appeared()
    page.basket_cost_message_appeared()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) 
    page.open()
    page.add_book_to_basket()
    page.success_message_not_present()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_book_to_basket()
    page.success_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.open_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_books_in_basket()
    basket_page.empty_basket_page_text_present()