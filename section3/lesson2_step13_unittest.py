import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'


class TestRegistration(unittest.TestCase):

    def test_registration2(self):
        wd = webdriver.Chrome()
        wd.get(link2)
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]').send_keys('First name')
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]').send_keys('Last name')
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]').send_keys('test@gmail.com')
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your phone:"]').send_keys('+73512537250')
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your address:"]').send_keys('Adress')
        wd.find_element(By.CSS_SELECTOR, "button.btn").click()
        # time.sleep(1)
        welcome_text = wd.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_registration1(self):
        wd = webdriver.Chrome()
        wd.get(link1)
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]').send_keys('First name')
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]').send_keys('Last name')
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]').send_keys('test@gmail.com')
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your phone:"]').send_keys('+73512537250')
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your address:"]').send_keys('Adress')
        wd.find_element(By.CSS_SELECTOR, "button.btn").click()
        #time.sleep(1)
        welcome_text = wd.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        #time.sleep(10)
        wd.quit()

if __name__ == "__main__":
    unittest.main()