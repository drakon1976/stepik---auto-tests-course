from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
    
sum = (int(browser.find_element_by_id('num1').text)+int(browser.find_element_by_id('num2').text))
browser.find_element_by_tag_name("select").click()
sum=str(sum)
print(sum)
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(sum)


button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(10)
browser.quit()

    
    