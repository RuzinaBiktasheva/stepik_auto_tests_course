import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test(app, url):
    s = ''
    link = 'https://stepik.org/lesson/' + url + '/step/1'
    app.helper.open_page(link)
    # явное ожидание textarea
    WebDriverWait(app.wd, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea'))
    )
    app.helper.calculation()
    # явное ожидание фидбека
    WebDriverWait(app.wd, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class="attempt-message_correct"]'))
    )
    # Проверка текста
    text = app.wd.find_element(By.CSS_SELECTOR, 'p[class="smart-hints__hint"]').text
    if text != 'Correct!':
        s += text
    print(s)
    time.sleep(10)