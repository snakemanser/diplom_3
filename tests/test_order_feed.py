import allure

from pages.main_page import MainPage
from pages.personal_acc_page import PersonalAccPage
from pages.order_page import OrderPage





class TestOrder:

    @allure.title(
        'Проверяет, что созданный заказ есть в списке заказов в работе')
    def test_order_in_orders_in_progress(self, driver, user_login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.wait_kratornaya_bulka()
        main_page.add_kratornaya_bulka()
        main_page.click_order_button()
        main_page.wait_modal_window_close()
        order_number = main_page.text_order_made_number()
        main_page.click_cross()
        main_page.click_order_feed()
        order_page.wait_order_in_progress()
        order_in_progress = order_page.text_order_in_progress()
        assert order_number in order_in_progress

    @allure.title(
        'Проверяет, что созданный заказ есть в списке заказов ленты заказов')
    def test_order_in_orders_feed(self, driver, user_login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.wait_kratornaya_bulka()
        main_page.add_kratornaya_bulka()
        main_page.click_order_button()
        main_page.wait_modal_window_close()
        order_number = main_page.text_order_made_number()
        main_page.click_cross()
        main_page.click_order_feed()
        order_page.wait_order_feed()
        order_page.click_order_by_number(order_number=int(order_number))

        element = order_page.find_order_details
        assert element

    @allure.title(
        'Проверяет, что заказ из истории заказов есть в списке заказов ленты заказов')
    def test_history_order_in_orders_feed(self, driver, user_login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        acc_page = PersonalAccPage(driver)

        main_page.wait_kratornaya_bulka()
        main_page.add_kratornaya_bulka()
        main_page.click_order_button()
        main_page.wait_modal_window_close()
        order_number = main_page.text_order_made_number()
        main_page.click_cross()
        main_page.click_personal_acc()
        acc_page.wait_text_pers_acc()
        acc_page.click_order_history_section()
        acc_page.wait_list_order()
        acc_page.find_order_by_number(order_number=order_number)
        acc_page.click_order_feed()
        order_page.wait_order_feed()
        order_page.click_order_by_number(order_number=int(order_number))

        element = order_page.find_order_details
        assert element

    @allure.title(
        'Проверяет, что количество заказов за все время увеличивается')
    def test_all_orders_qty_change(self, driver, user_login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_order_feed()
        order_page.wait_order_feed()
        orders_qty = order_page.all_orders_qty()
        order_page.click_constructor()
        main_page.wait_kratornaya_bulka()
        main_page.add_kratornaya_bulka()
        main_page.click_order_button()
        main_page.wait_modal_window_close()
        main_page.click_cross()
        main_page.click_order_feed()
        order_page.wait_order_feed()
        new_orders_qty = order_page.all_orders_qty()

        assert int(orders_qty) < int(new_orders_qty)

    @allure.title(
        'Проверяет, что количество заказов за сегодня  увеличивается')
    def test_today_orders_qty_change(self, driver, user_login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_order_feed()
        order_page.wait_order_feed()
        orders_qty = order_page.today_orders_qty()
        order_page.click_constructor()
        main_page.wait_kratornaya_bulka()
        main_page.add_kratornaya_bulka()
        main_page.click_order_button()
        main_page.wait_modal_window_close()
        main_page.click_cross()
        main_page.click_order_feed()
        order_page.wait_order_feed()
        new_orders_qty = order_page.today_orders_qty()

        assert int(orders_qty) < int(new_orders_qty)
