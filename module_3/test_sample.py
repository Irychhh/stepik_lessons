from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/ru/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    open = browser.find_element_by_id("login_link")
    open.click()

    address = "ishelter@mail.ru"

    email = browser.find_element_by_id("id_login-username")
    email.send_keys(address)

    password = browser.find_element_by_id("id_login-password")
    password.send_keys("zfdR88gMcgwxKD9")

    button = browser.find_element_by_name("login_submit")
    button.click()

    banner = browser.find_element_by_class_name("alertinner.wicon")
    assert banner.text == "Рады видеть вас снова"

    account = browser.find_element_by_class_name("icon-user")
    account.click()

    # открывает страницу профиля и сранивает почту с введенным адресом
    profil = browser.find_element_by_class_name("page-header")
    assert profil.text == "Профиль"

    element = browser.find_element_by_css_selector(".table tr:nth-child(2) > td")
    assert element.text == address

    # проверка кнопки Выход
    exit = browser.find_element_by_id("logout_link")
    assert exit.text == "Выход"



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
