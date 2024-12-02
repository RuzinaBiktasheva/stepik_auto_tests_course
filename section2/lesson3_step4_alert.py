from selenium.webdriver.common.by import By
from selenium import webdriver
import math

# инициализация браузера
wd = webdriver.Chrome()

try:
    # открытие страницы
    wd.get('http://suninjuly.github.io/alert_accept.html')
    # нажатие кнопки
    wd.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    #принятие confirm
    confirm = wd.switch_to.alert
    confirm.accept()
    # считывание значения
    x = int(wd.find_element(By.ID, 'input_value').text)
    # расчет математической функции
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    # введение ответа в текстовое поле
    value = calc(x)
    wd.find_element(By.ID, 'answer').send_keys(value)
    # нажатие кнопки Submit
    wd.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # получение кода
    alert = wd.switch_to.alert
    alert_text = alert.text[79:]
    print(alert_text)
    alert.accept()

finally:
    wd.quit()