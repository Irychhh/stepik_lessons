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


class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    PRODUCT_NAME_LOC = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_COST_LOC = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_BTN_ADD_TO_BASKET_LOC = (By.CSS_SELECTOR, ".btn-add-to-basket")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_IS_EMPTY_MESS = (By.CSS_SELECTOR, "#content_inner")
    ITEM_BASKET = (By.CSS_SELECTOR, ".basket-items")
    QUANTITY_LOC = (By.CSS_SELECTOR, "#id_form-0-quantity")
    SUBMIT_UPDATE = (By.CSS_SELECTOR, ".input-group-btn .btn.btn-default")


class SearchPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, "[type='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[value='Search']")
    MATCHING_FOUND_BOOK_NAME = (By.CSS_SELECTOR, ".page-header")
    MATCHING_FOUND_BOOK_COST = (By.CSS_SELECTOR, ".price_color")
    SEARCH_BTN_ADD_TO_BASKET_LOC = (By.CSS_SELECTOR, "[type='submit'].btn.btn-primary")
