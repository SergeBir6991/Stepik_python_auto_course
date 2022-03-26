from selenium import  webdriver
import time
link = "https://www.ozon.ru/"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/header/div[1]/div[3]/div/form/div[2]/input[1]")
input1.send_keys("star wars")
new_button = browser.find_element_by_css_selector("#stickyHeader > div.c3g > div > form > button > svg")
new_button.click()

time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()