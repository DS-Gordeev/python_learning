some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class MyIterator:

    def __init__(self, my_iter_list: list):
        self.my_iter_list = my_iter_list

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < len(self.my_iter_list):
            next_item = self.my_iter_list[self.counter]
            self.counter += 1
            return next_item
        else:
            raise StopIteration


a = MyIterator(some_list)

print(iter(a))

[print(i) for i in a]

