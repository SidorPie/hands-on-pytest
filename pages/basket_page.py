from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket not empty"

    def should_be_basket_empty_message(self):
        element = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert "Your basket is empty" in element.text, "No empty basket message"

