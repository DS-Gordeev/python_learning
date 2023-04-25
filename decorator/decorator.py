from datetime import datetime


# ОБЫЧНЫЙ ДЕКОРАТОР

def decor_time(func):
    def wrapper():
        print("Начало работы")
        func()
        print("Конец работы")
    return wrapper


@decor_time
def print_something():
    return print("Текущее время: {}".format(datetime.now()))

print_something()

print("\n_____________________________\n")

# ДЕКОРАТОР МОЖНО ВЫЗВАТЬ БЕЗ СИНТАКСИЧЕСКОГО САХАРА В ВИДЕ @

def print_something_2():
    return print("Текущее время: {}".format(datetime.now()))

print_something_2 = decor_time(print_something_2)
print_something_2()

print("\n_____________________________\n")

# ДЕКОРАТОР С ПЕРЕДАВАЕМЫМ АРГУМЕНТОМ

def decor_my_name(func):
    def wrapper(n):
        print("Начало работы")
        func(n)
        print("Конец работы")
    return wrapper

@decor_my_name
def print_my_name(name):
    print("Меня зовут " + name)

print_my_name('Dmitriy')

print("\n_____________________________\n")

# ДЕКОРАТОР С НЕСКОЛЬКИМИ АРГУМЕНТАМИ

def decor_my_name(func):
    def wrapper(n, s, a):
        print("Начало работы")
        func(n, s, a)
        print("Конец работы")
    return wrapper

@decor_my_name
def print_my_name_and_more(name, surname, age):
    print("Меня зовут " + name, surname + ". Мне " + age + " лет.")

print_my_name_and_more("Дмитрий", "Гордеев", "37")

print("\n_____________________________\n")

# ДЕКОРАТОР С ПРОИЗВОЛЬНЫМ КОЛ-ВОМ АРГУМЕНТОВ *args и **kwargs

def decor_my_name(func):
    def wrapper(*args, **kwargs):
        print("Начало работы")
        func(*args, **kwargs)
        print("Конец работы")
    return wrapper


@decor_my_name
def print_my_name_and_more(name, surname, age, gender='Мужчина'):
    print("Меня зовут " + name, surname + ". Мне " + age + " лет." + " Я " + gender)

print_my_name_and_more("Дмитрий", "Гордеев", "37", gender='Мужик!')

print("\n_____________________________\n")
