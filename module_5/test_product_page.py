from .pages.base_page import BasePage
from .pages.product_page import ProductPage

# import Pytest

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_url()
        page.should_be_name()
        page.should_be_cost()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.check_product_name()
        page.check_product_cost()
