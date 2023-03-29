from datetime import datetime


def decor(func):
    def wraper():
        print(datetime.now())
        func()
    return wraper


@decor
def print_something():
    return print('Строка')

print_something()

