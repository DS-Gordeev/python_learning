def add(value):
    return lambda param: param + value

add_to_100_function = add(100)
print(add_to_100_function)
a = add_to_100_function(5)  # 105
print(a)
b = add_to_100_function(50) # 150
print(b)