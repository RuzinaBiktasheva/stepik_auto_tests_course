from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# инициализация браузера
wd = webdriver.Chrome()

try:
    # открытие страницы
    wd.get('http://suninjuly.github.io/selects2.html')
    # расчет суммы заданных чисел
    num1 = int(wd.find_element(By.ID, 'num1').text)
    num2 = int(wd.find_element(By.ID, 'num2').text)
    sum = num1 + num2
    # выбор значения
    select = Select(wd.find_element(By.CSS_SELECTOR, 'select[class="custom-select"]'))
    select.select_by_visible_text(str(sum))
    # нажатие кнопки
    wd.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # получение кода
    alert = wd.switch_to.alert
    alert_text = alert.text[79:]
    print(alert_text)
    alert.accept()

finally:
    wd.quit()