from .base_page import BasePage
from selenium.webdriver.common.by import By

from .locators import BasketPageLocators


class BasketPage(BasePage):
    def mess_about_basket_is_empty(self):
        empty_mess_tmpl = "Your basket is empty. Continue shopping"

        mess_empty_basket = self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESS)
        assert mess_empty_basket, "No message that the cart is empty"

        actual_message_text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESS).text
        assert actual_message_text in empty_mess_tmpl, "Text does not match the expected"

    def basket_has_no_product(self):
        is_not_basket_has_products = self.is_not_element_present(*BasketPageLocators.ITEM_BASKET)
        assert is_not_basket_has_products, "Basket should not contain any goods, but it does"
