from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test(app):
    app.helper.open_page('https://stepik.org/lesson/236895/step/1')
    # явное ожидание textarea
    WebDriverWait(app.wd, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea'))
    )