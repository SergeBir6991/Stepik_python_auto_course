from selenium import webdriver
import time
link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()
browser.get(link)

elements = browser.find_elements_by_css_selector("[type = 'text']")
for element in elements:
    element.send_keys("Word")

add_button = browser.find_element_by_css_selector("body > div > form > button")
add_button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()