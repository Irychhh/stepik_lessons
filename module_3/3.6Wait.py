from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

    # Считать значение для переменной x
    browser.find_element_by_xpath("// span[contains( @ id, 'input_value')]")

    # Посчитать математическую функцию от x
    x_element = browser.find_element_by_xpath("// span[contains( @ id, 'input_value')]")
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле
    input = browser.find_element_by_xpath("//input[contains(@id,'answer')]")
    input.send_keys(y)

    # Нажать на кнопку "Submit"
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve")))
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
