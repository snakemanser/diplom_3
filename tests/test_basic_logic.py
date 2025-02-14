import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage





class TestBasicLogic:
    @allure.title(
        'Клик по кнопке "Лента заказов" открывает ленту заказов')
    def test_order_feed_redirect_to_order_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_order_feed()
        order_page.wait_order_feed()

        element = order_page.text_order_feed
        assert element

    @allure.title(
        'Клик по кнопке "Конструктор" открывает конструктор')
    def test_constructor_redirect_to_main_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_order_feed()
        order_page.click_constructor()

        element = main_page.find_enter_button
        assert element

    @allure.title(
        'Клик по ингредиенту открывает детали ингредиента')
    def test_click_ingredient_open_details(self, driver):
        main_page = MainPage(driver)

        main_page.click_kratornaya_bulka()

        element = main_page.text_ingredient_details()
        assert element

    @allure.title(
        'Клик по крестику закрывает детали ингредиента')
    def test_click_cross_close_details(self, driver):
        main_page = MainPage(driver)

        main_page.click_kratornaya_bulka()
        main_page.click_cross()

        element = main_page.find_enter_button
        assert element

    @allure.title(
        'Проверка изменения счетчика ингредиента')
    def test_ingredient_quantity_counter(self, driver):
        main_page = MainPage(driver)

        main_page.add_kratornaya_bulka()

        element = main_page.text_kratornaya_bulka_qty()
        assert int(element) == 2

    @allure.title(
        'Проверка оформления заказа')
    def test_user_make_order(self, driver, user_login):
        main_page = MainPage(driver)

        main_page.wait_kratornaya_bulka()
        main_page.add_kratornaya_bulka()
        main_page.click_order_button()

        element = main_page.text_started_cooking()
        assert element
