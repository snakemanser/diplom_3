import allure

from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.personal_acc_page import PersonalAccPage



class TestPersonalAcc:
    @allure.title(
        'Клик по кнопке "Личный кабинет" открывает личный кабинет')
    def test_personal_acc_redirect_to_personal_acc_page(self, driver, user_login):
        main_page = MainPage(driver)
        acc_page = PersonalAccPage(driver)

        main_page.click_personal_acc()
        acc_page.wait_text_pers_acc()

        element = acc_page.text_pers_acc
        assert element

    @allure.title(
        'Клик по "История заказов", открывает историю заказов')
    def test_open_order_history_list(self, driver, user_login):
        main_page = MainPage(driver)
        acc_page = PersonalAccPage(driver)

        main_page.click_personal_acc()
        acc_page.wait_text_pers_acc()
        acc_page.click_order_history_section()
        acc_page.wait_list_order()

        element = acc_page.find_list_order
        assert element

    @allure.title(
        'Клик по кнопке "Выход" открывает страницу авторизации')
    def test_button_logout_redirect_to_auth_page(self, driver, user_login):
        main_page = MainPage(driver)
        acc_page = PersonalAccPage(driver)
        auth_page = AuthPage(driver)

        main_page.click_personal_acc()
        acc_page.wait_text_pers_acc()
        acc_page.click_button_logout()
        auth_page.wait_text_entrance()

        element = auth_page.text_entrance
        assert element
