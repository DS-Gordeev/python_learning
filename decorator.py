from datetime import datetime


def decor(func):
    def wraper():
        print(datetime.now())
        return func()
    return wraper


@decor
def print_something():
    a = 'Some string'
    return a

b = print_something()
print(b)

