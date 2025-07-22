import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим элемент')
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Кликаем на элемент')
    def click_element(self, locator):
        self.find(locator).click()

    @allure.step('Ждем элемент')
    def wait_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Вставляем данные')
    def send_data(self, locator, data):
        self.find(locator).send_keys(data)

    @allure.step('Перетаскиваем элемент')
    def drag_and_drop_element(self, locator_start, locator_final):
        action = ActionChains(self.driver)
        element_start = self.find(locator_start)
        element_final = self.find(locator_final)
        action.drag_and_drop(element_start, element_final).perform()
