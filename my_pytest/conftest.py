import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Для FireFox
#firefox_service = FirefoxService(GeckoDriverManager().install())
#driver_firefox = webdriver.Firefox(service=firefox_service)

my_options = Options()
my_options.add_argument('start-maximized')
my_service = Service(ChromeDriverManager().install())

# Фикстура для запуска и закрытия драйвера
@pytest.fixture()
def setup():
    """Фикстура для запуска и закрытия веб-драйвера браузера Chrome"""
    driver = webdriver.Chrome(options=my_options, service=my_service)
    yield driver
    driver.close()

# Фикстура для тестирования scope
# scope='function' - by default
# scope='class'
# scope='module'
# scope='package'
# scope='session'
@pytest.fixture(scope='function')
def login_and_logout():
    """Тестовая фикстура для проверки параметра scope фикстуры"""
    print('Вход в систему выполнен')
    yield
    print('Выход из системы выполнен')