from selenium import webdriver
import math
import time
import os

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(2)
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

#ищем функцию
def calc(x):
	return str( math.log( abs( 12 * math.sin( int(x) ) ) ) )
    

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
otvet = browser.find_element_by_id('answer')
otvet.send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()


alert = browser.switch_to.alert
alert_text = alert.text.split()
alert.accept()
answer = alert_text[-1]
print(answer)

time.sleep(5)
browser.quit()

