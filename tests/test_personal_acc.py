import allure

from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.personal_acc_page import PersonalAccPage

from locators.auth_page_locators import AuthPageLocators
from locators.personal_acc_page_locators import PersonalAccPageLocators
from locators.header_locators import Headerlocators


class TestPersonalAcc:
    @allure.title(
        'Клик по кнопке "Личный кабинет" открывает личный кабинет')
    def test_personal_acc_redirect_to_personal_acc_page(self, driver, user_login):
        main_page = MainPage(driver)
        acc_page = PersonalAccPage(driver)

        main_page.click_element(Headerlocators.PERSONAL_ACC)
        acc_page.wait_element(PersonalAccPageLocators.MESS_PERSONAL_ACC_INFO)

        element = acc_page.find(PersonalAccPageLocators.MESS_PERSONAL_ACC_INFO).text
        assert element

    @allure.title(
        'Клик по "История заказов", открывает историю заказов')
    def test_open_order_history_list(self, driver, user_login):
        main_page = MainPage(driver)
        acc_page = PersonalAccPage(driver)

        main_page.click_element(Headerlocators.PERSONAL_ACC)
        acc_page.wait_element(PersonalAccPageLocators.MESS_PERSONAL_ACC_INFO)
        acc_page.click_order_history_section()
        acc_page.wait_element(PersonalAccPageLocators.LIST_ORDER_HISTORY)

        element = acc_page.find(PersonalAccPageLocators.LIST_ORDER_HISTORY)
        assert element

    @allure.title(
        'Клик по кнопке "Выход" открывает страницу авторизации')
    def test_button_logout_redirect_to_auth_page(self, driver, user_login):
        main_page = MainPage(driver)
        acc_page = PersonalAccPage(driver)
        auth_page = AuthPage(driver)

        main_page.click_element(Headerlocators.PERSONAL_ACC)
        acc_page.wait_element(PersonalAccPageLocators.MESS_PERSONAL_ACC_INFO)
        acc_page.click_button_logout()
        auth_page.wait_element(AuthPageLocators.MESS_ENTRANCE_LOGIN)

        element = auth_page.find(AuthPageLocators.MESS_ENTRANCE_LOGIN).text
        assert element
