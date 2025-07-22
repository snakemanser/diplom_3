from selenium.webdriver.common.by import By


class OrderPageLocators:

    MESS_ORDER_FEED = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")  # Текст "Лента заказов" в ленте заказов
    ORDER_DETAILS = (By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']") # Окно детали заказа
    ORDERS_ALL_TIME = (By.XPATH, "//div[@class='undefined mb-15']/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDERS_TODAY = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня:')]/parent::*/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDERS_IN_PROGRESS = (By.XPATH, "//p[text() = 'В работе:']/parent::div/ul[2]/li[@class='text text_type_digits-default mb-2']")
