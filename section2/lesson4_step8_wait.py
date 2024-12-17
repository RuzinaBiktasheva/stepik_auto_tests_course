from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test(app):
    # открытие страницы
    app.helper.open_page('http://suninjuly.github.io/explicit_wait2.html')
    # явное ожидание
    WebDriverWait(app.wd, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    # нажатие на кнопку Book
    app.wd.find_element(By.ID, 'book').click()
    # расчет математической функции
    value = app.helper.calc()
    # введение ответа в текстовое поле
    app.wd.find_element(By.ID, 'answer').send_keys(value)
    # нажатие кнопки Submit
    app.wd.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # получение кода
    app.helper.get_code()