from selenium import webdriver
import math
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
    
firstname=browser.find_element_by_name("firstname")
firstname.send_keys("Валерий")
lastname=browser.find_element_by_name("lastname")
lastname.send_keys("Иванов")
email=browser.find_element_by_name("email")
email.send_keys("valera@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element=browser.find_element_by_id('file')
element.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()


time.sleep(10)
browser.quit()
