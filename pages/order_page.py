import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.header_locators import Headerlocators


class OrderPage(BasePage):

    @allure.step('Получаем количество всех заказов')
    def all_orders_qty(self):
        qty = self.find(OrderPageLocators.ORDERS_ALL_TIME).text
        return qty

    @allure.step('Получаем количество заказов сегодня')
    def today_orders_qty(self):
        qty = self.find(OrderPageLocators.ORDERS_TODAY).text
        return qty

    @allure.step('Клик на номер заказа')
    def click_order_by_number(self, order_number):
        number = (By.XPATH, f"//p[contains(text(),'#0{order_number}')]")
        self.click_element(number)

    @allure.step('Ждем текст "Лента заказов"')
    def wait_order_feed(self):
        self.wait_element(OrderPageLocators.MESS_ORDER_FEED)

    @allure.step('Достаем текст "Лента заказов"')
    def text_order_feed(self):
        return self.find(OrderPageLocators.MESS_ORDER_FEED).text

    @allure.step('Клик конструктор')
    def click_constructor(self):
        self.click_element(Headerlocators.CONSTRUCTOR)

    @allure.step('Ждем заказы в работе')
    def wait_order_in_progress(self):
        self.wait_element(OrderPageLocators.ORDERS_IN_PROGRESS)

    @allure.step('Достаем номер заказа')
    def text_order_in_progress(self):
        return self.find(OrderPageLocators.ORDERS_IN_PROGRESS).text

    @allure.step('Находим окной деталей заказа')
    def find_order_details(self):
        self.find(OrderPageLocators.ORDER_DETAILS)

