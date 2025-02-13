import allure

from pages.main_page import MainPage
from pages.auth_page import AuthPage

from locators.auth_page_locators import AuthPageLocators

from faker import Faker



class TestPass:

    @allure.title(
        'Клик по ссылке "Восстановить пароль" открывает форму восстановления пароля')
    def test_link_forgot_pass_redirect_to_forgot_pass_form(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.click_enter_into_acc_button()
        auth_page.click_link_forgot_pass()

        element = auth_page.find(AuthPageLocators.TEXT_RECOVERY_PASS).text
        assert element

    @allure.title(
        'Клик по кнопке "Восстановить" открывает форму восстановления пароля')
    def test_restore_button_redirect_to_recovery_form(self, driver):
        email = Faker().email()

        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.click_enter_into_acc_button()
        auth_page.click_link_forgot_pass()
        auth_page.send_email_forgot_pass(email)
        auth_page.click_restore_button()
        auth_page.wait_element(AuthPageLocators.TEXT_CODE_FROM_EMAIL)

        element = auth_page.find(AuthPageLocators.TEXT_CODE_FROM_EMAIL).text
        assert element

    @allure.title(
        'Кнопка, которая показывает пароль, показывает пароль')
    def test_button_show_pass(self, driver):
        email = Faker().email()
        new_pass = Faker().password()

        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.click_enter_into_acc_button()
        auth_page.click_link_forgot_pass()
        auth_page.send_email_forgot_pass(email)
        auth_page.click_restore_button()
        auth_page.wait_element(AuthPageLocators.TEXT_CODE_FROM_EMAIL)
        auth_page.send_new_pass(new_pass)
        auth_page.click_button_show_pass()

        element = auth_page.find(AuthPageLocators.PASS_SHOWN)
        assert element
