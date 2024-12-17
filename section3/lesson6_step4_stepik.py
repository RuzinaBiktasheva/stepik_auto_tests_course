from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test(app):
    app.helper.open_page('https://stepik.org/lesson/236895/step/1')
    app.helper.login('email', 'password')
    # явное ожидание видимости кнопки
    WebDriverWait(app.wd, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.submit-submission'))
    )