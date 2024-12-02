from selenium.webdriver.common.by import By
from selenium import webdriver
import math

# инициализация браузера
wd = webdriver.Chrome()

try:
    # открытие страницы
    wd.get('https://suninjuly.github.io/math.html')
    # считывание значения
    x = int(wd.find_element(By.ID, 'input_value').text)
    # расчет математической функции
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    # введение ответа в текстовое поле
    value = calc(x)
    wd.find_element(By.ID, 'answer').send_keys(value)
    # выбор чек-бокса
    wd.find_element(By.ID, 'robotCheckbox').click()
    # выбор радиокнопки
    wd.find_element(By.ID, 'robotsRule').click()
    # нажатие кнопки Submit
    wd.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # получение кода
    alert = wd.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()
    # получение значения атрибута
    people_radio = wd.find_element(By.ID, "peopleRule").get_dom_attribute("checked")
    print(people_radio)
    # проверка
    assert people_radio == "true", "People radio is not selected by default"

finally:
    wd.quit()