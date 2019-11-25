import time
from selenium import webdriver


link = 'http://suninjuly.github.io/find_xpath_form'
driver = webdriver.Chrome()
driver.get(link)

formcontrol=driver.find_element_by_name("first_name")
formcontrol.send_keys("Валерий")
lastname=driver.find_element_by_name("last_name")
lastname.send_keys("Иванов")
firstname=driver.find_element_by_name("firstname")
firstname.send_keys("Калининград")
country=driver.find_element_by_id("country")
country.send_keys("РФ")

button = driver.find_element_by_xpath("//button[text()='Submit']")
button.click()
time.sleep(10)
driver.quit()
