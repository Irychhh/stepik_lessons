from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #Посчитать математическую функцию от x
    x_element = browser.find_element_by_id('input_value').text
    x_value = calc(x_element)
    #Проскроллить страницу вниз.
    button = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    #Ввести ответ в текстовое поле
    input = browser.find_element_by_id("answer")
    input.send_keys(x_value)
    #Выбрать checkbox "I'm the robot".
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    #Переключить radiobutton "Robots rule!".
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()
    #Нажать на кнопку "Submit".
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
