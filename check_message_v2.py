# проверка сообщения после нажатия кнопки (с явным ожиданием)
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# инициализация браузера
driver = WebDriver()

# открытие страницы браузера
driver.get("http://suninjuly.github.io/wait1.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

# нажатие на кнопку
button.click()

# получение текста сообщения
message = driver.find_element_by_id("verify_message")

# проверка, что текст сообщения соответствует ожидаемому
assert "successful" in message.text

print('Тест прошел успешно!')

driver.quit()