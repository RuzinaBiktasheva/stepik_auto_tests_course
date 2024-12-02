from selenium.webdriver.common.by import By
from selenium import webdriver
import os

# инициализация браузера
wd = webdriver.Chrome()

try:
    # открытие страницы
    wd.get('http://suninjuly.github.io/file_input')
    # заполнение полей
    wd.find_element(By.NAME, 'firstname').send_keys('Firstname')
    wd.find_element(By.NAME, 'lastname').send_keys('Lastname')
    wd.find_element(By.NAME, 'email').send_keys('email@com')
    # загрузка файла
    dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_name = os.path.join(dir_name, 'test.txt')
    wd.find_element(By.NAME, 'file').send_keys(file_name)
    # нажатие кнопки Submit
    wd.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # получение кода
    alert = wd.switch_to.alert
    alert_text = alert.text[80:]
    print(alert_text)
    alert.accept()

finally:
    wd.quit()