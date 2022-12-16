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

@pytest.mark.parametrize("number, data", [(1, 'первое значение'), (2, 'второе значение')])
def test_with_parametr(number, data):
    print(f'\nВывод на печать: {number}, {data}')



