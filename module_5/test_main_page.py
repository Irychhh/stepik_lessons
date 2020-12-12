from .pages.main_page import MainPage
#import Pytest

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        # открываем страницу
        page.open()
        # выполняем метод страницы - переходим на страницу логина
        page.go_to_login_page()
