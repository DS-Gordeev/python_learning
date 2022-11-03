import pytest


@pytest.fixture()
def setup():
    print('Вход в систему:')
    yield
    print('Делаем лог-аут')

def test_1(setup):
    print('123')

def test_2(setup):
    print('456')


