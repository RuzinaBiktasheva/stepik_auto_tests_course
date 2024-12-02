from selenium.webdriver.common.by import By
from selenium import webdriver

# инициализация браузера
wd = webdriver.Chrome()

try:
    # открытие страницы
    wd.get('https://suninjuly.github.io/huge_form.html')
    # заполнение формы
    elements = wd.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for element in elements:
        element.send_keys('Value')

    # нажатие кнопки
    wd.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # получение кода
    alert = wd.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()

finally:
    wd.quit()