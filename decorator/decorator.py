from datetime import datetime


def decor(func):
    def wrapper():
        print(datetime.now())
        func()
    return wrapper


@decor
def print_something():
    return print('Строка')

print_something()

