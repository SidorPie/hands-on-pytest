from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_add_to_cart(browser):
    page = ProductPage(browser,url="")  # Инициализируем объект Page Object
    page.open()                         # Открываем страницу в браузере
    page.should_be_add_to_cart_button() # Проверяем, что есть кнопка добавления в корзину
    page.add_product_to_cart()          # Жмем кнопку добавить в корзину 
    page.should_be_success_message()    # Проверяем, что есть сообщение с нужным текстом