from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):

    # проверка соответствия урла
    def should_be_product_url(self):
        assert '/?promo=newYear' in self.browser.current_url, "Incorrect URL"
        assert True

    # проверка названия карточки товара
    def should_be_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_LOC), "Name of Product card is not presented"

    # проверка стоимости карточки товара
    def should_be_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST_LOC), "Cost of Product card is not presented"

    # проверка добавления в корзину
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_BTN_ADD_TO_BASKET_LOC)
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_BTN_ADD_TO_BASKET_LOC), "Button Add to Basket is not presented"
        button_add_to_basket.click()

    # поверка наименования добавленного товара
    def check_product_name(self):
        actual_product_name = self.browser.find_element(By.CSS_SELECTOR, ".alert:nth-child(1) strong").text
        expected_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LOC).text
        print("Actual product name is " + actual_product_name, "Expected product name is " + expected_product_name)
        assert actual_product_name == expected_product_name

    # поверка стоимости добавленного товара
    def check_product_cost(self):
        actual_product_price = self.browser.find_element(By.CSS_SELECTOR, ".alertinner>p>strong").text
        expected_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_COST_LOC).text
        print("Actual product price is " + actual_product_price, "Expected product price is " + expected_product_price)
        assert actual_product_price == expected_product_price
