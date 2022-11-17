import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

my_options = Options()
my_options.add_argument('start-maximized')
my_service = Service(ChromeDriverManager().install())

#@pytest.fixture(scope='session')
def setup():
    browser = webdriver.Chrome(options=my_options, service=my_service)
    yield browser
    browser.quit()