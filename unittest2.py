from selenium import webdriver
import time
import unittest

def link_t(link):
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

    time.sleep(1)
    return browser.find_element_by_tag_name("h1").text


class Test1(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!", "Error Registration 1")


    def test_reg2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"), "Congratulations! You have successfully registered!", "registration is failed")

if __name__ == "__main__":
    unittest.main()

time.sleep(2)
    # закрываем браузер после всех манипуляций
browser.quit()