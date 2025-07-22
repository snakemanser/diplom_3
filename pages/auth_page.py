import allure
from pages.base_page import BasePage

from locators.auth_page_locators import AuthPageLocators




class AuthPage(BasePage):
    @allure.step('Клик по ссылке "Восстановить пароль"')
    def click_link_forgot_pass(self):
        self.click_element(AuthPageLocators.LINK_FORGOT_PASS)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_restore_button(self):
        self.click_element(AuthPageLocators.BUTTON_RESTORE)

    @allure.step('Вводим мейл')
    def send_email_forgot_pass(self, email):
        self.send_data(AuthPageLocators.FIELD_EMAIL_FORGOT_PASS, data=email)

    @allure.step('Вводим пароль')
    def send_new_pass(self, new_pass):
        self.send_data(AuthPageLocators.FIELD_NEW_PASS, data=new_pass)

    @allure.step('Клик по кнопке, которая показывает пароль')
    def click_button_show_pass(self):
        self.click_element(AuthPageLocators.BUTTON_SHOW_PASS)

    @allure.step('Достаем текст "Восстановление пароля"')
    def text_recovery_pass(self):
        return self.find(AuthPageLocators.TEXT_RECOVERY_PASS).text

    @allure.step('Ждем текст "Введите код из письма"')
    def wait_text_code_from_email(self):
        self.wait_element(AuthPageLocators.TEXT_CODE_FROM_EMAIL)

    @allure.step('Достаем текст "Введите код из письма"')
    def text_code_from_email(self):
        return self.find(AuthPageLocators.TEXT_CODE_FROM_EMAIL).text

    @allure.step('Находим пароль')
    def find_pass_shown(self):
        self.find(AuthPageLocators.PASS_SHOWN)

    @allure.step('Ждем текст "Вход"')
    def wait_text_entrance(self):
        self.wait_element(AuthPageLocators.MESS_ENTRANCE_LOGIN)

    @allure.step('Достаем текст "Вход"')
    def text_entrance(self):
        return self.find(AuthPageLocators.MESS_ENTRANCE_LOGIN).text
