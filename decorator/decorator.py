from datetime import datetime


def decor(func):
    def wrapper():
        print("Начало работы")
        func()
        print("Конец работы")
    return wrapper


@decor
def print_something():
    return print("Текущее время: {}".format(datetime.now()))

print_something()

print("\n_____________________________\n")

def print_something_2():
    return print("Текущее время: {}".format(datetime.now()))

# Еще декоратор можно вызвать без синтаксического сахара в виде @

decor_result = decor(print_something_2)
decor_result()


