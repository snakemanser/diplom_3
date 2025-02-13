import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


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

