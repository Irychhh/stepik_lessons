from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators, SearchPageLocators, LoginPageLocators


class SearchPage(BasePage):
    # проверка перехода на страницу результатов поиска
    def go_to_search_page(self, book_name):
        input_search_field = self.browser.find_element(*SearchPageLocators.SEARCH_FIELD)
        input_search_field.send_keys(book_name)
        submit_search = self.browser.find_element(*SearchPageLocators.SEARCH_BUTTON)
        submit_search.click()

    # проверка соответствия урла страницы результатов поиска
    def should_be_search_url(self):
        assert '/search/?q=The+shellcoder%27s+handbook' in self.browser.current_url, "Incorrect URL"
        assert True

    def should_be_search_page(self):
        assert self.is_element_present(*SearchPageLocators.MATCHING_SEARCH_BOOK_NAME), "Search book name is not " \
                                                                                       "presented, "

    # поверка наименования найденного товара
    def should_be_search_book_name(self, book_name):
        assert book_name in self.browser.find_element(*SearchPageLocators.MATCHING_SEARCH_BOOK_NAME).text, "Incorrect book name"
        assert True

    # проверка добавления в корзину со страницы результатов поиска
    def add_to_basket_from_search_page(self):
            button_add_to_basket = self.browser.find_element(*SearchPageLocators.SEARCH_BTN_ADD_TO_BASKET_LOC)
            assert self.is_element_present(*SearchPageLocators.SEARCH_BTN_ADD_TO_BASKET_LOC), "Button Add to Basket is not presented"
            button_add_to_basket.click()

    # проверка названия и стоимости добавленного товара

