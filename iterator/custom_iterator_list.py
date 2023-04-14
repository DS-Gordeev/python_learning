class Tumb:

    def __init__(self):
        self.boxes = {1: [], 2: [], 3: []}

    def __str__(self):
        return f'В наших тумбочках лежит:\n' \
               f'В первой: {self.boxes[1]}\n' \
               f'Во второй: {self.boxes[2]}\n' \
               f'В третьей: {self.boxes[3]}\n'
    #   Что итерируем
    def __iter__(self):
        self.all_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
        self.a = 0
        # Метод __iter__ должен обязательно возвращать сам себя
        return self

    #  Как итерируем, по каким правилам
    def __next__(self):
        if self.a < len(self.all_items):
            x = self.all_items[self.a]
            self.a += 1
            return x
        #  Обязательно объявляем исключение StopIteration, иначе не выйдем из бесконечного цикла :--> None
        raise StopIteration


    def add_to_box(self, box_num: int,  obj):
        self.boxes[box_num].append(obj)

    def remove_from_box(self, box_num):
        self.boxes[box_num].pop()

my_tumb = Tumb()

my_tumb.add_to_box(1, 'ножницы')
my_tumb.add_to_box(1, 'карандаш')
my_tumb.add_to_box(2, 'блокнот')
my_tumb.add_to_box(2, 'скотч')
my_tumb.add_to_box(3, 'камера')
my_tumb.add_to_box(3, 'телефон')

for i in my_tumb:
    print(i)






