class Multiplication:

    def __iter__(self):
        self.a = 1
        # Метод __iter__ должен обязательно возвращать сам себя
        return self


    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        #  Обязательно объявляем исключение StopIteration, иначе не выйдем из бесконечного цикла :--> None
        raise StopIteration

obj = Multiplication()

# В цикле for неявно вызывается встроенная функция iter(obj) для объекта.
# Она вернет итератор __iter__, который будет использоваться для прохода по элементам списка.
# Затем будет вызываться функция next(iter(obj)) для полученного итератора
# и каждый раз будет возвращаться новое значение до тех пор, пока не возникнет ошибка StopIteration
for i in obj:
    print(i)