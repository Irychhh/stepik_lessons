import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
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
    result.implicitly_wait(5)
    result.user_language = language

    yield result

    print("\nquit browser..")
    result.quit()
