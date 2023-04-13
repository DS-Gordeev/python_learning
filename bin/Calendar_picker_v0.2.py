from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import datetime

###
### Необходимо установить webdriver-manager выполнив команду:
### pip install webdriver-manager
###

options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://demoqa.com/date-picker')

# Выбираем календарь
driver.find_element(By.ID, 'datePickerMonthYearInput').click()
time.sleep(3)

# Определяем текущую дату + 10 дней
today = datetime.datetime.today()
delta = datetime.timedelta(days=10)
future = today + delta
print(future.day)

# Выбираем дату в календаре
calendar_date = driver.find_elements(By.XPATH, f'//div[@class="react-datepicker__week"]/div[text()="{str(future.day)}"]')
# Если на открытой вкладке две одинаковые даты разных месяцев, то выбирает вторую из будущего
if len(calendar_date) == 2:
    calendar_date[1].click()
else:
    calendar_date[0].click()

time.sleep(3)