import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators



class MainPage(BasePage):
    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_enter_into_acc_button(self):
        self.click_element(MainPageLocators.BUTTON_ENTER_INTO_ACC)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_order_button(self):
        self.click_element(MainPageLocators.BUTTON_ORDER)

    @allure.step('Клик по краторной булке')
    def click_kratornaya_bulka(self):
        self.click_element(MainPageLocators.KRATORNAYA_BULKA)

    @allure.step('Клик на крестик')
    def click_cross(self):
        self.click_element(MainPageLocators.CROSS)
