from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()
    def should_be_adding_to_cart_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_CART), "Message about adding to cart is not presented"
    def should_be_message_with_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_CART_PRICE), "Message with cart price is not presented"
    def is_cart_price_correct(self):
        expected_price = self.browser.find_element(*ProductPageLocators.MESSAGE_CART_PRICE_VALUE).text
        actual_price = self.browser.find_element(*ProductPageLocators.ACTUAL_BOOK_PRICE).text
        assert expected_price == actual_price, "Cart price not equal book price"
    def is_adding_message_correct(self):
        expected_book_name = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_CART_BOOK_NAME).text
        actual_book_name = self.browser.find_element(*ProductPageLocators.ACTUAL_BOOK_NAME).text
        assert expected_book_name == actual_book_name, "Added to cart book name incorrect "

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_CART), \
            "Success message is presented, but should not be"
    def should_be_message_disappeared_after_awhile(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_CART), \
            "Success message is presented, but should not be"