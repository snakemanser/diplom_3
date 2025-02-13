import pytest
from selenium import webdriver
from locators.main_page_locators import MainPageLocators
from locators.auth_page_locators import AuthPageLocators


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise ValueError('Unknown browser type')
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()

# Фикстура логина тестового юзера 5го спринта
@pytest.fixture
def user_login(driver):
    driver.find_element(*MainPageLocators.BUTTON_ENTER_INTO_ACC).click()
    driver.find_element(*AuthPageLocators.LOGIN_EMAIL).send_keys('vitaliy.shmulyaev.16322@qa.qa')
    driver.find_element(*AuthPageLocators.LOGIN_PASS).send_keys('123456')
    driver.find_element(*AuthPageLocators.BUTTON_LOGIN).click()
    return driver
