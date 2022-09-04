from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import datetime as dt

options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# Можно использовать не опцию, а встроенный в Selenium метод maximize_window(), нужно убрать options=options
# driver.maximize_window()

driver.get('http://demoqa.com')

# Text Box
text_box_url = 'https://demoqa.com/text-box'
user_data = {'user_name': 'Marazmator',
            'user_email': 'test@mail.ru',
            'current_adress': 'Moscow',
            'permanent_adress': 'Sherbakovskaya street, 32/7, app. 10'}

# Переходим в раздел Elements
driver.find_element(By.CSS_SELECTOR, 'div.card.mt-4.top-card').click() # Переходим в раздел Elements
# Выбираем подраздел Text Box
driver.find_element(By.XPATH, '//li[@id="item-0"]/span[contains(., "Text Box")]').click()
# Проверяем, что мы в разделе Text Box
assert driver.current_url == text_box_url, 'Current URL id wrong'
# Обновляем страницу
driver.refresh()

driver.find_element(By.ID, 'userName').send_keys(user_data['user_name'])

# Нажатиея на клавишу BACKSPACE для очистки поля ввода
# driver.find_element(By.ID, 'userName').send_keys(Keys.BACKSPACE * 10)

# Очистка поля методом clear()
# driver.find_element(By.ID, 'userName').clear()

driver.find_element(By.ID, 'userEmail').send_keys(user_data['user_email'])
driver.find_element(By.ID, 'currentAddress').send_keys(user_data['current_adress'])
driver.find_element(By.ID, 'permanentAddress').send_keys(user_data['permanent_adress'])
driver.find_element(By.CSS_SELECTOR, 'button#submit').click()

# Прокрутка окна браузера вниз на указанное кол-во пикселей
#driver.execute_script("window.scrollTo(0, 500)")

# Прокрутка окна браузера до определенного элемента ActionChains
action = ActionChains(driver)
elem = driver.find_element(By.CSS_SELECTOR, 'div.element-group:nth-child(5) span.group-header div.header-wrapper')
action.scroll_to_element(elem).perform()

# Делаем скриншот экрана
date_format = dt.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
driver.save_screenshot(f'./screenshots/text_box_screenshot {date_format}.png')

assert user_data['user_name'] in driver.find_element(By.CSS_SELECTOR, 'div#output p#name').text, 'Wrong username output'
assert user_data['user_email'] in driver.find_element(By.CSS_SELECTOR, 'div#output p#email').text, 'Wrong email output'
assert user_data['current_adress'] in driver.find_element(By.CSS_SELECTOR, 'div#output p#currentAddress').text, 'Wrong currentAddress output'
assert user_data['permanent_adress'] in driver.find_element(By.CSS_SELECTOR, 'div#output p#permanentAddress').text, 'Wrong permanentAddress output'


# Check Box

#driver.find_element(By.XPATH, '//li[@id="item-1"]/span[contains(., "Check Box")]').click()
#driver.find_element(By.CSS_SELECTOR, 'button[title="Expand all"]').click()
#time.sleep(1)
#driver.find_element(By.CSS_SELECTOR, 'button[title="Collapse all"]').click()
#driver.find_element(By.CSS_SELECTOR, 'ol li button:first-child').click()

driver.close()