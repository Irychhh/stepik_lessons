from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'http://selenium1py.pythonanywhere.com/' in self.browser.current_url, "Incorrect URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_EMAIL), "E-mail is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_PASSWORD), "PASSWORD is not presented"
        assert self.is_element_present(*LoginPageLocators.GET_LOGIN_BTN_SUBMIT), "LOGIN BUTTON is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_LOC), "E-mail is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_LOC), "Password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT_LOC), "Repeat password is not " \
                                                                                             "presented "
        assert self.is_element_present(*LoginPageLocators.GET_REGISTRATION_BTN_LOC), "Registration button is not " \
                                                                                     "presented "

    def register_new_user(self, email, password):
        input1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_LOC)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_LOC)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT_LOC)
        input3.send_keys(password)
        submit_register = self.browser.find_element(*LoginPageLocators.GET_REGISTRATION_BTN_LOC)
        submit_register.click()
