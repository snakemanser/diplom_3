from selenium.webdriver.common.by import By


class MainPageLocators:

    BUTTON_ENTER_INTO_ACC = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")  # Кнопка "Войти в аккаунт"
    BUTTON_ORDER = (By.XPATH, "//button[@class ='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")  # Кнопка "Оформить заказ"
    KRATORNAYA_BULKA = (By.XPATH, "//img[@alt='Краторная булка N-200i']") # Краторная булка
    KRATORNAYA_BULKA_QUANTITY_COUNTER = (By.XPATH, "//ul[@class='BurgerIngredients_ingredients__list__2A-mT'][1]/*[2]/div[1]/p")  # Краторная булка счетчик количества
    MESS_INGREDIENT_DETAILS = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]") # Текст "Детали ингредиента" в карточке ингредиента
    CROSS = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']/*") # Крестик в карточке ингредиента
    MODAL_CLOSE = (By.XPATH, "//div[@class= 'Modal_modal__P3_V5']") # Окно при оформлении заказа
    CONSTRUCTOR_BURGER = (By.XPATH, "//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']") # Конструктор бургера
    MESS_STARTED_COOKING = (By.XPATH, "//p[contains(text(),'Ваш заказ начали готовить')]") # Текст "Ваш заказ начали готовить" в окне с инфо об оформленном заказе
    ORDER_MADE_NUMBER = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
