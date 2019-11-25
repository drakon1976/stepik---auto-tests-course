import math
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://suninjuly.github.io/find_link_text")
link = driver.find_element_by_partial_link_text("224592")
link.click()
formcontrol=driver.find_element_by_css_selector(".form-control")
formcontrol.send_keys("Валерий")
lastname=driver.find_element_by_name("last_name")
lastname.send_keys("Иванов")
firstname=driver.find_element_by_name("firstname")
firstname.send_keys("Калининград")
country=driver.find_element_by_id("country")
country.send_keys("РФ")
button = driver.find_element_by_css_selector("button.btn")
button.click()
time.sleep(10)
driver.quit()
