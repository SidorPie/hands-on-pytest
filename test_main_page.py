from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


# def test_add_to_cart(browser):
#     page = ProductPage(browser,url="")  # Инициализируем объект Page Object
#     page.open()                         # Открываем страницу в браузере
#     page.should_be_add_to_cart_button() # Проверяем, что есть кнопка добавления в корзину
#     page.add_product_to_cart()          # Жмем кнопку добавить в корзину 
#     page.should_be_success_message()    # Проверяем, что есть сообщение с нужным текстом