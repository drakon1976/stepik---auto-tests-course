from selenium import webdriver
import time
import unittest

class Test1(unittest.TestCase):
    def test1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)    
        input1 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group first_class']//input")
        input1.send_keys("Valera")
        input2 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group second_class']//input")
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group third_class']//input")
        input3.send_keys("Ivanov@mail.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(3)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text_elt.text, "Congratulations! You have successfully registered!", 'Error Registration 1')
    
    
    def test2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)   
        input1 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group first_class']//input")
        input1.send_keys("Valera")
        input2 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group second_class']//input")
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group third_class']//input")
        input3.send_keys("Ivanov@mail.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(3)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text_elt.text, "Congratulations! You have successfully registered!", 'Error Registration 2')
        
        
if __name__ == "__main__":
    unittest.main()
    
   
time.sleep(5)

    
    