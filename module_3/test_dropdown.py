from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_value_text = browser.find_element_by_id("num1").text

    second_value_text = browser.find_element_by_id("num2").text

    sum = int(first_value_text) + int(second_value_text)
    sum_value = str(sum)

    # browser.find_element_by_tag_name("select").click()
    # browser.find_element_by_css_selector("[value= /sum_value/").click()

    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum_value)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
