import allure

from pages.main_page import MainPage
from pages.personal_acc_page import PersonalAccPage
from pages.order_page import OrderPage

from locators.main_page_locators import MainPageLocators
from locators.personal_acc_page_locators import PersonalAccPageLocators
from locators.order_page_locators import OrderPageLocators
from locators.header_locators import Headerlocators




class TestOrder:

    @allure.title(
        'Проверяет, что созданный заказ есть в списке заказов в работе')
    def test_order_in_orders_in_progress(self, driver, user_login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.wait_element(MainPageLocators.KRATORNAYA_BULKA)
        main_page.drag_and_drop_element(locator_start=MainPageLocators.KRATORNAYA_BULKA,
                                        locator_final=MainPageLocators.CONSTRUCTOR_BURGER)
        main_page.click_order_button()
        main_page.wait_element(MainPageLocators.MODAL_CLOSE)
        order_number = main_page.find(MainPageLocators.ORDER_MADE_NUMBER).text
        main_page.click_element(MainPageLocators.CROSS)
        main_page.click_element(Headerlocators.ORDER_FEED)
        order_page.wait_element(OrderPageLocators.ORDERS_IN_PROGRESS)
        order_in_progress = order_page.find(OrderPageLocators.ORDERS_IN_PROGRESS).text
        assert order_number in order_in_progress

    @allure.title(
        'Проверяет, что созданный заказ есть в списке заказов ленты заказов')
    def test_order_in_orders_feed(self, driver, user_login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.wait_element(MainPageLocators.KRATORNAYA_BULKA)
        main_page.drag_and_drop_element(locator_start=MainPageLocators.KRATORNAYA_BULKA,
                                        locator_final=MainPageLocators.CONSTRUCTOR_BURGER)
        main_page.click_order_button()
        main_page.wait_element(MainPageLocators.MODAL_CLOSE)
        order_number = main_page.find(MainPageLocators.ORDER_MADE_NUMBER).text
        main_page.click_element(MainPageLocators.CROSS)
        main_page.click_element(Headerlocators.ORDER_FEED)
        order_page.wait_element(OrderPageLocators.MESS_ORDER_FEED)
        order_page.click_order_by_number(order_number=int(order_number))

        element = order_page.find(OrderPageLocators.ORDER_DETAILS)
        assert element

    @allure.title(
        'Проверяет, что заказ из истории заказов есть в списке заказов ленты заказов')
    def test_history_order_in_orders_feed(self, driver, user_login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        acc_page = PersonalAccPage(driver)

        main_page.wait_element(MainPageLocators.KRATORNAYA_BULKA)
        main_page.drag_and_drop_element(locator_start=MainPageLocators.KRATORNAYA_BULKA,
                                        locator_final=MainPageLocators.CONSTRUCTOR_BURGER)
        main_page.click_order_button()
        main_page.wait_element(MainPageLocators.MODAL_CLOSE)
        order_number = main_page.find(MainPageLocators.ORDER_MADE_NUMBER).text
        main_page.click_element(MainPageLocators.CROSS)
        main_page.click_element(Headerlocators.PERSONAL_ACC)
        acc_page.wait_element(PersonalAccPageLocators.MESS_PERSONAL_ACC_INFO)
        acc_page.click_order_history_section()
        acc_page.wait_element(PersonalAccPageLocators.LIST_ORDER_HISTORY)
        acc_page.find_order_by_number(order_number=order_number)
        acc_page.click_element(Headerlocators.ORDER_FEED)
        order_page.wait_element(OrderPageLocators.MESS_ORDER_FEED)
        order_page.click_order_by_number(order_number=int(order_number))

        element = order_page.find(OrderPageLocators.ORDER_DETAILS)
        assert element

    @allure.title(
        'Проверяет, что количество заказов за все время увеличивается')
    def test_all_orders_qty_change(self, driver, user_login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_element(Headerlocators.ORDER_FEED)
        order_page.wait_element(OrderPageLocators.MESS_ORDER_FEED)
        orders_qty = order_page.all_orders_qty()
        order_page.click_element(Headerlocators.CONSTRUCTOR)
        main_page.wait_element(MainPageLocators.KRATORNAYA_BULKA)
        main_page.drag_and_drop_element(locator_start=MainPageLocators.KRATORNAYA_BULKA,
                                        locator_final=MainPageLocators.CONSTRUCTOR_BURGER)
        main_page.click_order_button()
        main_page.wait_element(MainPageLocators.MODAL_CLOSE)
        main_page.click_element(MainPageLocators.CROSS)
        main_page.click_element(Headerlocators.ORDER_FEED)
        order_page.wait_element(OrderPageLocators.MESS_ORDER_FEED)
        new_orders_qty = order_page.all_orders_qty()

        assert int(orders_qty) < int(new_orders_qty)

    @allure.title(
        'Проверяет, что количество заказов за сегодня  увеличивается')
    def test_today_orders_qty_change(self, driver, user_login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_element(Headerlocators.ORDER_FEED)
        order_page.wait_element(OrderPageLocators.MESS_ORDER_FEED)
        orders_qty = order_page.today_orders_qty()
        order_page.click_element(Headerlocators.CONSTRUCTOR)
        main_page.wait_element(MainPageLocators.KRATORNAYA_BULKA)
        main_page.drag_and_drop_element(locator_start=MainPageLocators.KRATORNAYA_BULKA,
                                        locator_final=MainPageLocators.CONSTRUCTOR_BURGER)
        main_page.click_order_button()
        main_page.wait_element(MainPageLocators.MODAL_CLOSE)
        main_page.click_element(MainPageLocators.CROSS)
        main_page.click_element(Headerlocators.ORDER_FEED)
        order_page.wait_element(OrderPageLocators.MESS_ORDER_FEED)
        new_orders_qty = order_page.today_orders_qty()

        assert int(orders_qty) < int(new_orders_qty)


