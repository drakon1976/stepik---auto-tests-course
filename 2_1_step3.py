from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

#ищем функцию
def calc(x):
	return str( math.log( abs( 12 * math.sin( int(x) ) ) ) )
    
    
treasure = browser.find_element_by_id('treasure')
x = treasure.get_attribute('valuex')
y = calc(x)

otvet = browser.find_element_by_id('answer')
otvet.send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

option2 = browser.find_element_by_id("robotsRule")
option2.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(10)
browser.quit()

    
    