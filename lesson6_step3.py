import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://suninjuly.github.io/simple_form_find_task.html")
formcontrol=driver.find_element_by_css_selector(".form-control")
formcontrol.send_keys("Валерий")
lastname=driver.find_element_by_name("last_name")
lastname.send_keys("Иванов")
firstname=driver.find_element_by_name("firstname")
firstname.send_keys("Калининград")
country=driver.find_element_by_id("country")
country.send_keys("РФ")
submitbutton=driver.find_element_by_id("submit_button")
submitbutton.click()
time.sleep(10)
driver.quit()



    lastname=browser.find_element_by_name("form-control second")
    lastname.send_keys("Иванов")
    firstname=browser.find_element_by_name("form-control third")
    firstname.send_keys("Email@wrtrg.ru")
    country=browser.find_element_by_id("country")
    country.send_keys("РФ")
 # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    