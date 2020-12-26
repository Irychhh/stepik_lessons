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

    @pytest.mark.parametrize('book_name',
                             ["The shellcoder's handbook",
                              "Hacking Exposed Wireless",
                              "Coders at Work",
                              pytest.param("Studyguide for Counter Hack", marks=pytest.mark.xfail),
                              "Gray Hat Hacking",
                              "Reversing",
                              "Applied cryptography",
                              "Hacker's Delight",
                              "Silence On The Wire",
                              "Google Hacking"])
    def test_guest_can_go_to_search_many_page(self, browser, book_name):
        # Data
        link = "http://selenium1py.pythonanywhere.com"
        book_name = f"{book_name}"
        template = "{} has been added to your basket."
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page = SearchPage(browser, link)
        page.go_to_search_page(book_name)
        page.should_be_search_page()
        page.should_be_search_book_name(book_name)
        page.add_to_basket_from_search_page()
        # Assert
        page = ProductPage(browser, link)
        page.check_add_to_basket_notification(book_name, template)

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

    class TestUserAddToBasketFromSearchPage:
        @pytest.fixture(scope="function", autouse=True)
        def setup(self, browser):
            # Data
            link_login = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
            email = "ishelter@mail.ru"
            password = "zfdR88gMcgwxKD9"
            # Arrange
            page = LoginPage(browser, link_login)
            page.open()
            # Act
            page.login_user(email, password)
            # Assert
            page.should_be_authorized_user()

        def test_user_can_add_and_clear_into_basket_found_products_(self, browser):
            # Data
            link = "http://selenium1py.pythonanywhere.com"
            book_name = "The shellcoder's handbook"
            # Arrange
            page = MainPage(browser, link)
            page.open()
            # Act
            page = SearchPage(browser, link)
            page.go_to_search_page(book_name)
            page.should_be_search_url()
            page.should_be_search_page()
            page.should_be_search_book_name(book_name)
            page.add_to_basket_from_search_page()
            page.go_to_basket()
            basket_page = BasketPage(browser, browser.current_url)
            basket_page.clear_basket()
            # Assert
            basket_page.basket_has_no_product()
            basket_page.mess_about_basket_is_empty()

        def test_user_can_change_quantity_products_into_basket(self, browser):
            # Data
            link = "http://selenium1py.pythonanywhere.com"
            book_name = "The shellcoder's handbook"
            # Arrange
            page = MainPage(browser, link)
            page.open()
            # Act
            page = SearchPage(browser, link)
            page.go_to_search_page(book_name)
            page.should_be_search_url()
            page.should_be_search_page()
            page.should_be_search_book_name(book_name)
            page.add_to_basket_from_search_page()
            page.go_to_basket()
            basket_page = BasketPage(browser, browser.current_url)
            # Assert
            basket_page.addition_products()
            basket_page.clear_basket()
            basket_page.basket_has_no_product()
            basket_page.mess_about_basket_is_empty()
