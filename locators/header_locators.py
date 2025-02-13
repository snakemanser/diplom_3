from selenium.webdriver.common.by import By


class Headerlocators:

    CONSTRUCTOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]")  # Конструктор
    ORDER_FEED = (By.XPATH, "//p[contains(text(),'Лента Заказов')]") # Лента заказов
    PERSONAL_ACC = (By.XPATH, "//a[@href='/account']")  # Личный кабинет