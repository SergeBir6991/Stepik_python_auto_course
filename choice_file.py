from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//input[@placeholder = "Enter first name"]')
    input1.send_keys("AAA")
    input2 = browser.find_element_by_xpath('//input[@placeholder = "Enter last name"]')
    input2.send_keys("BBB")
    input3 = browser.find_element_by_xpath('//input[@placeholder = "Enter email"]')
    input3.send_keys("CCC")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_css_selector("[type='file']")
    element.send_keys(file_path)

    add_button = browser.find_element_by_xpath('//button')
    add_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
