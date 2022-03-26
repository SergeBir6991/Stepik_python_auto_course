import math
import time
from selenium import webdriver
browser = webdriver.Chrome()

link = "http://suninjuly.github.io/find_xpath_form"
browser.get(link)

input1 = browser.find_element_by_xpath('/html/body/div[1]/form/div[1]/input')
input1.send_keys("Ivan")
input2 = browser.find_element_by_xpath('/html/body/div[1]/form/div[2]/input')
input2.send_keys("Petrov")
input3 = browser.find_element_by_xpath('//html/body/div[1]/form/div[3]/input')
input3.send_keys("Smolensk")
input4 = browser.find_element_by_xpath('/html/body/div[1]/form/div[4]/input')
input4.send_keys("Russia")
button = browser.find_element_by_xpath("/html/body/div[1]/form/div[6]/button[3]")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()