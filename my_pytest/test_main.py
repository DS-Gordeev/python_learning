import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Из фикстуры приходит драйвер, а в конце закрывает браузер
def test_start(setup):
    setup.get('http://ya.ru')

# Обработка ошибки через assert
def test_scope_1(login_and_logout):
    a = 2
    b = 2
    print('Значения a и b должны совпадать')
    assert a == b, 'Значение a и b НЕ совпадают!'

# Обработка ошибки через pytest.fail()
def test_scope_2(login_and_logout):
    a = 1
    b = 2
    time.sleep(2.58)
    print('Значения a и b должны быть разные')
    if a == b:
        pytest.fail('Значение a и b совпадают!')

# Принимает фикстуру с указанием имени name="ultimate_answer"
def test_number(ultimate_answer):
    assert ultimate_answer == 42

# ПАРАМЕТРИЗАЦИЯ ФУНКЦИИ
# Декоратор parametrize принимает строку и список картежей (если одно значение, то может быть просто список)
# Происходит перебор значений из строки и картежа которые подставляются в тест
# Например: number - 1, data - первое значение и т.д.
# По итогу получается кол-во тестов равное кол-ву пар значений. Тесты не зависимы друг от друга.
@pytest.mark.parametrize("number, data",
[
    (1, 'first value'),
    (2, 'second value')
])
def test_with_function_params(number, data):
    print(f'\nВывод на печать: {number}, {data}')

# ПАРАМЕТРИЗАЦИЯ ЧЕРЕЗ ФИКСТУРУ
# Из фикстуры check_urls получаем значение URL разных сайтов
def test_with_fixture_params(setup, check_urls):
    print(f'\nТестируем сайт: {check_urls}')
    setup.get(check_urls)
    print(f'\nТест пройдет успешно')

# ПАРАМЕТРИЗАЦИЯ ЧЕРЕЗ ХУК pytest_generate_tests
def pytest_generate_tests(metafunc):
    if "start_url" in metafunc.fixturenames:
        metafunc.parametrize("start_url", ["http://ya.ru", "http://rambler.ru", "http://mail.ru"])
    elif "start" in metafunc.fixturenames:
        metafunc.parametrize("start", ["http://dev.ppdp.ru"])

def test_with_hook_params(setup, start_url):
    print(f'\nТестируем сайт: {start_url}')
    setup.get(start_url)
    print(f'\nТест пройдет успешно')





