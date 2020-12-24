import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-GB',
                      help='Choose GUI language for tests')


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    if language not in ["ru", 'en-GB', 'es', 'fr']:
        raise pytest.UsageError("The wrong language is selected on the page")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print("\nstart browser for test..")

    result = webdriver.Chrome(options=options)
    result.maximize_window()
    result.implicitly_wait(7)
    result.user_language = language

    yield result

    print("\nquit browser..")
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    result.save_screenshot('Screenshots/screenshot-%s.png' % now)
    result.quit()
