import pytest
import time
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

LANGUAGE_DICT = {
    "ru": {"add_to_basket_btn_text": "Добавить в корзину", "add_to_basket_notification_tmp": "{} был добавлен в "
                                                                                             "вашу корзину", "Empty "
                                                                                                             "basket": "Ваша корзина пуста Продолжить покупки"},
    "en_GB": {"add_to_basket_btn_text": "Add to basket", "add_to_basket_notification_tmp": "{} has been added to your "
                                                                                           "basket.",
              "Empty basket": "Your basket is empty. Continue shopping"},
}


class TestProductPage:

    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo"
                                           "=offer7", marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        # Data
        # expected_lang_code = browser.user_language
        # template = LANGUAGE_DICT[expected_lang_code: = {add_to_basket_notification_tmp}]
        product_name = "Coders at Work"
        template = "{} has been added to your basket."
        # Arrange
        link = f"{link}"
        page = ProductPage(browser, link)
        page.open()
        # Act
        # page.should_be_product_url()
        page.should_be_name()
        page.should_be_cost()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        # Assert
        page.check_add_to_basket_notification(product_name, template)
        page.check_product_cost()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message_is_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Arrange
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        # Assert
        basket_page.basket_has_no_product()
        basket_page.mess_about_basket_is_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Data
        link_login = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = "zxcasdqweQWERTY"
        # Arrange
        page = LoginPage(browser, link_login)
        page.open()
        # Act
        page.register_new_user(email, password)
        # Assert
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        # Data
        # expected_lang_code = browser.user_language
        template = LANGUAGE_DICT.get('ru', {}).get('add_to_basket_notification_tmp', "")
        product_name = "Coders at Work"
        #template = "{} has been added to your basket."
        # Arrange
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        # Act
        # page.should_be_product_url()
        page.should_be_name()
        page.should_be_cost()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        # Assert
        page.check_add_to_basket_notification(product_name, template)
        page.check_product_cost()
