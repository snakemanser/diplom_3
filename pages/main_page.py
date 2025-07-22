import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.header_locators import Headerlocators



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

    @allure.step('Клик на личный кабинет')
    def click_personal_acc(self):
        self.click_element(Headerlocators.PERSONAL_ACC)

    @allure.step('Клик на лента заказов')
    def click_order_feed(self):
        self.click_element(Headerlocators.ORDER_FEED)

    @allure.step('Ищем кнопку "Войти в аккаунт"')
    def find_enter_button(self):
        self.find(MainPageLocators.BUTTON_ENTER_INTO_ACC)

    @allure.step('Достаем текст "Детали ингредиента"')
    def text_ingredient_details(self):
        return self.find(MainPageLocators.MESS_INGREDIENT_DETAILS).text

    @allure.step('Добавляем краторную булку!"')
    def add_kratornaya_bulka(self):
        self.drag_and_drop_element(locator_start=MainPageLocators.KRATORNAYA_BULKA,
                                   locator_final=MainPageLocators.CONSTRUCTOR_BURGER)

    @allure.step('Достаем количество краторных булок')
    def text_kratornaya_bulka_qty(self):
        return self.find(MainPageLocators.KRATORNAYA_BULKA_QUANTITY_COUNTER).text

    @allure.step('Достаем текст "Ваш заказ начали готовить"')
    def text_started_cooking(self):
        return self.find(MainPageLocators.MESS_STARTED_COOKING).text

    @allure.step('Ждем краторную булку')
    def wait_kratornaya_bulka(self):
        self.wait_element(MainPageLocators.KRATORNAYA_BULKA)

    @allure.step('Ждем прогрузку окна об успешном оформлении заказа')
    def wait_modal_window_close(self):
        self.wait_element(MainPageLocators.MODAL_CLOSE)

    @allure.step('Достаем номер заказа')
    def text_order_made_number(self):
        return self.find(MainPageLocators.ORDER_MADE_NUMBER).text

