import pytest
from .pages.product_page import ProductPage
import time


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
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019/?promo=offer8"
    page = ProductPage(browser, link)
    page.open()
    page.add_book_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.book_added_to_basket_message_appeared()
    page.basket_cost_message_appeared()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    
    page = ProductPage(browser, link) 
    page.open()
    page.add_book_to_basket() 
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    pass

def test_guest_cant_see_success_message(browser, link):

    page = ProductPage(browser, link)
    page.open() 
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    pass

def test_message_disappeared_after_adding_product_to_basket(browser, link):
    
    page = ProductPage(browser, link)
    page.open()
    page.add_book_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    pass