import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Для FireFox
# firefox_service = FirefoxService(GeckoDriverManager().install())
# driver_firefox = webdriver.Firefox(service=firefox_service)

my_options = Options()
my_options.add_argument('start-maximized')
my_service = Service(ChromeDriverManager().install())


@pytest.fixture(scope='function')
def setup():
    """Фикстура для запуска и закрытия веб-драйвера браузера Chrome
    Возвращает объект driver через yield
    """
    driver = webdriver.Chrome(options=my_options, service=my_service)
    yield driver
    driver.close()


@pytest.fixture(scope='function')
def login_and_logout():
    """Тестовая фикстура для проверки параметра scope фикстуры
    # scope='function' - by default
    # scope='class'
    # scope='module'
    # scope='package'
    # scope='session'
    """
    print('\nВход в систему выполнен')
    yield
    print('\nВыход из системы выполнен')


@pytest.fixture(autouse=True, scope='function')
def duration_test():
    """Фикстура для указания времени выполнения теста. Применяется автоматически"""
    start = time.time()
    yield
    stop = time.time()
    delta = str(stop - start)
    print(f'\nВремя выполнения теста: {delta[0:4]} секунд')


@pytest.fixture(name="ultimate_answer")
def other_fixture_name():
    """Фикстура с указанием имени для теста test_number"""
    return 42


@pytest.fixture(params=["http://ya.ru", "http://rambler.ru", "http://mail.ru"])
def check_urls(request):
    """Фикстура с параметрами для теста test_with_fixture_params
    Передает параметры params через request.param по одному"""
    return request.param


def pytest_generate_tests(metafunc):
    """Хук для параметризации теста test_with_hook_params"""
    if "start_url" in metafunc.fixturenames:
        metafunc.parametrize("start_url", ["http://ya.ru", "http://rambler.ru", "http://mail.ru"])
    elif "start" in metafunc.fixturenames:
        metafunc.parametrize("start", ["http://dev.ppdp.ru"])
