def closure_example():

    x = 5

    def inner_func():
        print(x)
    return inner_func

a = closure_example()
print(a())