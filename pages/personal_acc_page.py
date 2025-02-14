import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.personal_acc_page_locators import PersonalAccPageLocators
from locators.header_locators import Headerlocators



class PersonalAccPage(BasePage):
    @allure.step('Клик по "История заказов"')
    def click_order_history_section(self):
        self.click_element(PersonalAccPageLocators.SECTION_ORDER_HISTORY)

    @allure.step('Клик по кнопке "Выйти"')
    def click_button_logout(self):
        self.click_element(PersonalAccPageLocators.BUTTON_LOGOUT)

    @allure.step('Находим заказ по номеру')
    def find_order_by_number(self, order_number):
        number = (By.XPATH, f"//p[contains(text(),'#0{order_number}')]")
        self.find(number)

    @allure.step('Ждем текст "В этом разделе вы можете изменить свои персональные данные"')
    def wait_text_pers_acc(self):
        self.wait_element(PersonalAccPageLocators.MESS_PERSONAL_ACC_INFO)

    @allure.step('Достаем текст "В этом разделе вы можете изменить свои персональные данные"')
    def text_pers_acc(self):
        return self.find(PersonalAccPageLocators.MESS_PERSONAL_ACC_INFO).text

    @allure.step('Ждем загрузки истории заказов')
    def wait_list_order(self):
        self.wait_element(PersonalAccPageLocators.LIST_ORDER_HISTORY)

    @allure.step('Находим контейнер истории заказов')
    def find_list_order(self):
        self.find(PersonalAccPageLocators.LIST_ORDER_HISTORY)

    @allure.step('Клик по ленте заказов')
    def click_order_feed(self):
        self.click_element(Headerlocators.ORDER_FEED)
