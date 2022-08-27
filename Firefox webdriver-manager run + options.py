from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.add_argument("--kiosk")

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
# Можно использовать не опцию, а встроенный в Selenium метод maximize_window(), нужно убрать options=options
# driver.maximize_window()

driver.get('http://yandex.ru')
driver.close()

