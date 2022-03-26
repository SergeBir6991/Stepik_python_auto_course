from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('[id = "input_value"]')
    x = x_element.text
    y = calc(x)


    input1 = browser.find_element_by_xpath("//input")
    input1.send_keys(y)
    input2 = browser.find_element_by_css_selector("[type = 'checkbox']")
    input2.click()
    input3 = browser.find_element_by_css_selector('[id="robotsRule"]')
    input3.click()
    add_button = browser.find_element_by_xpath('//button')
    add_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

