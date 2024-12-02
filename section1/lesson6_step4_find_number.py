from selenium.webdriver.common.by import By
from selenium import webdriver

# инициализация браузера
wd = webdriver.Chrome()

try:
    # открытие страницы
    wd.get('https://suninjuly.github.io/simple_form_find_task.html')
    # заполнение формы
    wd.find_element(By.NAME, 'first_name').click()
    wd.find_element(By.NAME, 'first_name').send_keys('First_name')
    wd.find_element(By.NAME, 'last_name').click()
    wd.find_element(By.NAME, 'last_name').send_keys('Last_name')
    wd.find_element(By.CSS_SELECTOR, "input[class='form-control city']").click()
    wd.find_element(By.CSS_SELECTOR, "input[class='form-control city']").send_keys('City')
    wd.find_element(By.ID, "country").click()
    wd.find_element(By.ID, "country").send_keys('Country')
    # нажатие кнопки
    wd.find_element(By.ID, 'submit_button').click()
    # получение кода
    alert = wd.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()

finally:
    wd.quit()