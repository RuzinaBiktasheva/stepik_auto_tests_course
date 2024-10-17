# проверка сообщения после нажатия кнопки (с неявным ожиданием)
from selenium.webdriver.chrome.webdriver import WebDriver

# инициализация браузера
driver = WebDriver()

# открытие страницы браузера
driver.get("http://suninjuly.github.io/wait1.html")

# не явное ожидание
driver.implicitly_wait(5)

# поиск кнопки
button = driver.find_element_by_id("verify")

# нажатие на кнопку
button.click()

# получение текста сообщения
message = driver.find_element_by_id("verify_message")

# проверка, что текст сообщения соответствует ожидаемому
assert "successful" in message.text

print('Тест прошел успешно!')

driver.quit()