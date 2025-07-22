from selenium.webdriver.common.by import By


class AuthPageLocators:

    LINK_FORGOT_PASS = (By.XPATH, "//a[@href='/forgot-password']")  # Ссылка "Восстановить пароль" в форме авторизации
    TEXT_RECOVERY_PASS = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]") # Текст "Восстановление пароля" в форме восстановления пароля
    FIELD_EMAIL_FORGOT_PASS = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")  # Поле ввода мейла в форме восстановления пароля
    BUTTON_RESTORE = (By.XPATH, "//button[contains(text(),'Восстановить')]") # Кнопка восстановить в форме восстановления пароля
    TEXT_CODE_FROM_EMAIL = (By.XPATH, "//label[contains(text(),'Введите код из письма')]") # Текст "Введите код из письма" в форме восстановления пароля
    FIELD_NEW_PASS = (By.XPATH, "//input[@name='Введите новый пароль']")  # Поле ввода пароля в форме восстановления пароля
    BUTTON_SHOW_PASS = (By.XPATH, "//div[@class='input__icon input__icon-action']")  # Кнопка, которая показывает введенный пароль
    PASS_SHOWN = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")  # Текст пароля в поле ввода пароля, в форме восстановления пароля
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")  # Кнопка "Войти"
    LOGIN_EMAIL = (By.XPATH, "//label[contains(text(), 'Email')]/parent::*/input")  # Поле авторизации email
    LOGIN_PASS = (By.XPATH, "//label[contains(text(), 'Пароль')]/parent::*/input")  # Поле авторизации пароль
    MESS_ENTRANCE_LOGIN = (By.XPATH, "//h2[contains(text(),'Вход')]")  # Текст "Вход" на странице авторизации

