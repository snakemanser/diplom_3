from selenium.webdriver.common.by import By


class PersonalAccPageLocators:

    MESS_PERSONAL_ACC_INFO = (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']")  # Текст "В этом разделе вы можете изменить свои персональные данные" в личном кабинете
    SECTION_ORDER_HISTORY = (By.XPATH, "//a[contains(text(),'История заказов')]") # История заказов в личном кабинете
    LIST_ORDER_HISTORY = (By.XPATH, "//div[@class='OrderHistory_orderHistory__qy1VB']") # Список истории заказов разделе истории заказов
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(),'Выход')]")  # Кнопка "Выход" в личном кабинете
