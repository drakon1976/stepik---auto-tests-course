from selenium import webdriver
import math
import time

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
    
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#button = browser.find_element_by_tag_name("button")
#browser.execute_script("window.scrollBy(0, 150);")
button = browser.find_element_by_css_selector('button[type="submit"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

otvet = browser.find_element_by_id('answer')
otvet.send_keys(y)
option1 = browser.find_element_by_id("robotCheckbox")
option1.click()
option2 = browser.find_element_by_id('robotsRule')
option2.click()
button.click()

time.sleep(10)
browser.quit()

    
    