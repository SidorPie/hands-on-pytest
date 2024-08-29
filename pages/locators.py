from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
class ProductPageLocators():
    ACTUAL_BOOK_NAME = (By.CSS_SELECTOR,"div.product_main h1" )
    ACTUAL_BOOK_PRICE = (By.CSS_SELECTOR,"div.product_main p.price_color" )
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,"button.btn-add-to-basket" )
    MESSAGE_ADD_TO_CART = (By.CSS_SELECTOR,"div#messages > :nth-child(1)" )
    MESSAGE_ADD_TO_CART_BOOK_NAME = (By.CSS_SELECTOR,"div#messages > :nth-child(1) strong" )
    MESSAGE_CART_PRICE = (By.CSS_SELECTOR,"div#messages > :nth-child(3)" )
    MESSAGE_CART_PRICE_VALUE = (By.CSS_SELECTOR,"div#messages > :nth-child(3) strong" )