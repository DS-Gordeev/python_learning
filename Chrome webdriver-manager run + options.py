from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# Можно использовать не опцию, а встроенный в Selenium метод maximize_window(), нужно убрать options=options
# driver.maximize_window()

driver.get('http://demoqa.com')

time.sleep(2)
driver.close()