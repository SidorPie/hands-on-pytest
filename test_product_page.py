from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time

# links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail(reason="Some bug")),
#                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
#
# links =  ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]


# @pytest.mark.parametrize('link',links)
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    # page.solve_quiz_and_get_code()
    page.should_be_adding_to_cart_message()
    page.should_be_message_with_price()
    page.is_adding_message_correct()
    page.is_cart_price_correct()

# Падает, потому что проверяет отсутствие сообщения о добавлении товара в корзину
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    # page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

# Проходит, так как после добавления в корзину должно быть сообщение
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

# Не проходит, так как сообщение не исчезает
@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    # page.solve_quiz_and_get_code()
    page.should_be_message_disappeared_after_awhile()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # Проверка что тест падает, если в корзине что-то есть
    # page.add_to_cart()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_empty()
    basket_page.should_be_basket_empty_message()

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        passwd = str(time.time())
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(email,passwd)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.should_be_adding_to_cart_message()
        page.should_be_message_with_price()
        page.is_adding_message_correct()
        page.is_cart_price_correct()