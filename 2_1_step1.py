from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

try:    
    otvet = browser.find_element_by_id('answer')
    otvet.send_keys(y)
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()
   
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    
finally:

    time.sleep(10)
    browser.quit()
    
    