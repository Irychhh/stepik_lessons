import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.search_page import SearchPage

link = "http://selenium1py.pythonanywhere.com/"


class TestSearchFromMainPage():
    def test_guest_can_go_to_search_page(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com"
        book_name = "The shellcoder's handbook"
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page = SearchPage(browser, link)
        page.go_to_search_page(book_name)
        # Assert
        page.should_be_search_url()
        page.should_be_search_page()
        page.should_be_search_book_name(book_name)

    def test_guest_can_add_to_basket_from_search_page(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com"
        book_name = "The shellcoder's handbook"
        template = "{} has been added to your basket."
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page = SearchPage(browser, link)
        page.go_to_search_page(book_name)
        page.should_be_search_url()
        page.should_be_search_page()
        page.should_be_search_book_name(book_name)
        # Assert
        page.add_to_basket_from_search_page()
        page = ProductPage(browser, link)
        page.check_add_to_basket_notification(book_name, template)
        #page.check_product_cost()