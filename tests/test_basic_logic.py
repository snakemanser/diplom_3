import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from locators.header_locators import Headerlocators




class TestBasicLogic:
    @allure.title(
        'Клик по кнопке "Лента заказов" открывает ленту заказов')
    def test_order_feed_redirect_to_order_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_element(Headerlocators.ORDER_FEED)
        order_page.wait_element(OrderPageLocators.MESS_ORDER_FEED)

        element = order_page.find(OrderPageLocators.MESS_ORDER_FEED).text
        assert element

    @allure.title(
        'Клик по кнопке "Конструктор" открывает конструктор')
    def test_constructor_redirect_to_main_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_element(Headerlocators.ORDER_FEED)
        order_page.click_element(Headerlocators.CONSTRUCTOR)

        element = main_page.find(MainPageLocators.BUTTON_ENTER_INTO_ACC)
        assert element

    @allure.title(
        'Клик по ингредиенту открывает детали ингредиента')
    def test_click_ingredient_open_details(self, driver):
        main_page = MainPage(driver)

        main_page.click_kratornaya_bulka()

        element = main_page.find(MainPageLocators.MESS_INGREDIENT_DETAILS).text
        assert element

    @allure.title(
        'Клик по крестику закрывает детали ингредиента')
    def test_click_cross_close_details(self, driver):
        main_page = MainPage(driver)

        main_page.click_kratornaya_bulka()
        main_page.click_cross()

        element = main_page.find(MainPageLocators.BUTTON_ENTER_INTO_ACC)
        assert element

    @allure.title(
        'Проверка изменения счетчика ингредиента')
    def test_ingredient_quantity_counter(self, driver):
        main_page = MainPage(driver)

        main_page.drag_and_drop_element(locator_start=MainPageLocators.KRATORNAYA_BULKA,
                                        locator_final=MainPageLocators.CONSTRUCTOR_BURGER)

        element = main_page.find(MainPageLocators.KRATORNAYA_BULKA_QUANTITY_COUNTER).text
        assert int(element) == 2

    @allure.title(
        'Проверка оформления заказа')
    def test_user_make_order(self, driver, user_login):
        main_page = MainPage(driver)

        main_page.wait_element(MainPageLocators.KRATORNAYA_BULKA)
        main_page.drag_and_drop_element(locator_start=MainPageLocators.KRATORNAYA_BULKA,
                                        locator_final=MainPageLocators.CONSTRUCTOR_BURGER)
        main_page.click_order_button()

        element = main_page.find(MainPageLocators.MESS_STARTED_COOKING).text
        assert element
