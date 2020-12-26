from .base_page import BasePage
from selenium.webdriver.common.by import By

from .locators import BasketPageLocators, ProductPageLocators


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

    # очищение корзины
    def clear_basket(self):
        input1 = self.browser.find_element(*BasketPageLocators.QUANTITY_LOC)
        input1.clear()
        input1.send_keys('0')
        submit_update = self.browser.find_element(*BasketPageLocators.SUBMIT_UPDATE)
        submit_update.click()

    # увеличение количества товаров в корзине
    def addition_products(self):
        input1 = self.browser.find_element(*BasketPageLocators.QUANTITY_LOC)
        input1.clear()
        input1.send_keys('10')
        submit_update = self.browser.find_element(*BasketPageLocators.SUBMIT_UPDATE)
        submit_update.click()
        # assert input1.text == "10", "Incorrect quantity of products"




