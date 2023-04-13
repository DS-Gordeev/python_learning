import pytest

@pytest.fixture()
def setup_1():
    print('Вход в систему:')
    yield
    print('Делаем лог-аут')

def test_1(setup_1):
    print('123')

def test_2(setup_1):
    print('456')


