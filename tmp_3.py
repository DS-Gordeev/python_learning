import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

###
### Необходимо установить webdriver-manager выполнив команду:
### pip install webdriver-manager
###

options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

# Словарь с логинами пользователей
login_dict = {'Стандартный': 'standard_user',
              'Заблокированный': 'locked_out_user',
              'Проблемный': 'problem_user',
              'Ожидание входа': 'performance_glitch_user'}

# Один пароль для всех пользователей
password = 'secret_sauce'
i = 0
for login in login_dict:

    driver.find_element(By.ID, 'user-name').send_keys(Keys.BACKSPACE * 20)
    driver.find_element(By.ID, 'password').send_keys(Keys.BACKSPACE * 20)
    driver.find_element(By.ID, 'user-name').send_keys(login_dict.get(login))
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()
    current_url = driver.current_url

    # Если логин был совершен успешно, то делаем логаут
    if current_url == 'https://www.saucedemo.com/inventory.html':
        driver.find_element(By.ID, 'react-burger-menu-btn').click()
        driver.find_element(By.ID, 'logout_sidebar_link').click()
        assert base_url == driver.current_url, f'Не удалось вернуться на начальную страницу {base_url}'
        user_type = list(login_dict.keys())
        print(f'Логин и логаут для пользователя "{user_type[i]}" с логином: {login_dict.get(login)} и паролем: {password} выполнен успешно!\n')

    # Если логин не был выполнен, то выводим ошибку
    else:
        error_text = driver.find_element(By.CSS_SELECTOR, 'div.error-message-container').text
        driver.find_element(By.CSS_SELECTOR, 'button.error-button').click()
        user_type = list(login_dict.keys())
        print(f'Логин для пользователя "{user_type[i]}" с логином: {login_dict.get(login)} и паролем: {password} НЕ выполнен!\nОшибка: {error_text}\n')

    i += 1

#Тест завершен
print('Тест выполнен успешно!')
driver.quit()





