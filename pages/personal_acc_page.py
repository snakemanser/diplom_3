import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.personal_acc_page_locators import PersonalAccPageLocators



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
