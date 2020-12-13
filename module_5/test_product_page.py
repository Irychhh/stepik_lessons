import pytest
from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

LANGUAGE_DICT = {
    "ru": {"add_to_basket_btn_text": "Добавить в корзину", "add_to_basket_notification_tmp": "{} был добавлен в "
                                                                                             "вашу корзину"},
    "en_GB": {"add_to_basket_btn_text": "Add to basket", "add_to_basket_notification_tmp": "{} has been added to your "
                                                                                           "basket."},
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
        # product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LOC).text
        product_name = "Coders at Work"
        template = "{} был добавлен в вашу корзину."
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
