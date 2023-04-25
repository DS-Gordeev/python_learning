from datetime import datetime
from functools import wraps

# Обернутая функция теряет свои значения __name__ и __doc__ т.к. ссылается уже на функцию-декоратор

def decor_time(func):
    def wrapper():
        print("Начало работы")
        func()
        print("Конец работы")
    return wrapper

@decor_time
def print_something():
    """
    Функция печатает текущее время
    """
    return print("Текущее время: {}".format(datetime.now()))

print_something()
# Вывод __name__ и __doc__ для функции wrapper, а не print_something, т.к. print_something уже ссылается на wrapper
print(print_something.__name__)  # wrapper
print(print_something.__doc__)   # None

print("\n_____________________________\n")

# Переопределение методово __name__ и __doc__ для декорируемой функции

def decor_time_redefinition(func):
    def wrapper():
        print("Начало работы")
        func()
        print("Конец работы")
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

@decor_time_redefinition
def print_something():
    """
    Функция печатает текущее время
    """
    return print("Текущее время: {}".format(datetime.now()))

print_something()
# Вывод __name__ и __doc__ для функции print_something, т.к. мы их переопределили
print(print_something.__name__)  # print_something
print(print_something.__doc__)   # Функция печатает текущее время

print("\n_____________________________\n")

# Переопределение методово __name__ и __doc__ при помощи декоратора @wraps(func), не забываем про его импорт

def decor_time_wraps(func):
    @wraps(func)
    def wrapper():
        print("Начало работы")
        func()
        print("Конец работы")
    return wrapper

@decor_time_wraps
def print_something():
    """
    Функция печатает текущее время
    """
    return print("Текущее время: {}".format(datetime.now()))

print_something()
# Вывод __name__ и __doc__ для функции print_something, т.к. мы их переопределили при помощи декоратора @wraps
print(print_something.__name__)  # print_something
print(print_something.__doc__)   # Функция печатает текущее время
