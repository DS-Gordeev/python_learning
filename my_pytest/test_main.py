import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

chrome_options = Options()
chrome_options.add_argument('start-maximized')
chrome_service = Service(ChromeDriverManager().install())

# Для FireFox
#firefox_service = FirefoxService(GeckoDriverManager().install())
#driver_firefox = webdriver.Firefox(service=firefox_service)

# Фикстура для передачи и закрытия драйвера
@pytest.fixture()
def setup():
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    yield driver
    driver.close()

def test_1(setup):
    setup.get('http://ya.ru')



