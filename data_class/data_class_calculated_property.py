from dataclasses import dataclass, field, InitVar


class Vector3D:

    def __init__(self, x, y, z, calculate: bool = True):
        self.x = x
        self.y = y
        self.z = z
        # Свойство result тут является вычисляемым
        self.result = (x * x + y * y + z * z) * 10 if calculate else 0

obj = Vector3D(1, 2, 3)
print(obj.result)  # 140

print("\n_____________________________\n")

@dataclass
class VectorData3D:
     # repr=False - свойство не будет выведено на печать, т.к. будет убрано из __repr__
     # compare=False - свойство не будет принимать участие при сравнении объектов, т.к. будет убрано из __eq__
     # init=False - свойство не будет принимать участие в вычисление в инициализаторе дата-класса
     x: int = field(repr=False)
     y: int = field(compare=False)
     z: int
     # Аннотируем calculate классом InitVar и свойство calculate автоматически передается в __post_init__,
     # где уже реализуем необходимую логику
     calculate: InitVar[bool] = True
     result: int = field(init=False)

     # Инициализатор дата-класса в конце свое работы вызовет метод __post_init__ где и будет рассчитан result
     def __post_init__(self, calculate):
         self.result = (self.x * self.x + self.y * self.y + self.z * self.z) * 10 if calculate else 0

obj_data = VectorData3D(4, 5, 6)
# При печати объекта obj_data не будет выведено значение result, т.к. в метод __repr__ попадает только то,
# что прописано в инициализаторе. Для этого применим функцию field() c параметром init=False,
# т.к. нам нужно только значение result, а не его вычисление в инициализаторе дата-класса.
print(obj_data)

print("\n_____________________________\n")

# order=True добавляет неявное определение методов сравнения в дата-класс

@dataclass(order=True)
class Person:
     first_name: str = "Ahmed"
     last_name: str = "Besbes"
     age: int = 30
     job: str = "Data Scientist"

p1 = Person(age=30)
p2 = Person(age=20)

print(p1 > p2)  # True
