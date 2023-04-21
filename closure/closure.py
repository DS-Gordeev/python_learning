# Замыкание (closure) в Python - это вложенная функция, которая запоминает значения из объемлющей области видимости,
# даже если эта область видимости больше не существует.
# Это означает, что замыкание может использовать переменные из функции, в которой оно определено,
# даже если эта функция уже завершила свою работу.


# Первый пример _______________________________

def closure_example():
    x = 5
    # Это замыкание, т.к. вызов функции inner_func() после вызова closure_example() вернет 5
    def inner_func():
        print(x)

    return inner_func

a = closure_example()
a()

# Второй пример _______________________________

def counter():
    count = 0

    def current():
        # Ключевое слово nonlocal указывает на то, что переменная cnt находится в объемлющей области видимости,
        # а не в локальной области видимости функции current() и мы может ее изменять.
        nonlocal count
        count += 1
        print(count)

    return current


closure_function = counter()
closure_function()  # 1
closure_function()  # 2
closure_function()  # 3

# Третий пример ______________________________

def add_number(x):
    # После вызова функции add_number(x) с параметром, значение этого параметра сохранится. И при последующем вызове
    # вложенной функции add(y) (т.е. объекта add_five()) произойдет сложение этих параметров (return x + y)
    def add(y):
        return x + y
    return add

add_five = add_number(5)
print(add_five(3)) # выводит 8

# Четвертый пример ___________________________

# Замыкание с lambda функцией

def add(value):
    return lambda param: param + value

value_100 = add(100)
# Тут вызывается lambda функцией с сохраненным значением value=100 которое суммируется с param=50
print(value_100(50))
