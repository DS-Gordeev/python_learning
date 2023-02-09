from datetime import datetime


def decor(func):
    def wraper(arg):
        func(arg)
        print(datetime.now())
    return wraper


@decor
def print_something(string_to_print):
    return print(string_to_print)

print_me = 'new'

#print_something(print_me)

