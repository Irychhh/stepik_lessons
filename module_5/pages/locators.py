from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_USERNAME_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_USERNAME_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    GET_LOGIN_BTN_SUBMIT = (By.CSS_SELECTOR, "[name='login_submit']")

    REGISTRATION_EMAIL_LOC = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_LOC = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT_LOC = (By.CSS_SELECTOR, "#id_registration-password2")
    GET_REGISTRATION_BTN_LOC = (By.CSS_SELECTOR, "[name='registration_submit']")
