from dataclasses import dataclass, field
# Особенности при указании в инициализаторе свойства со значением по умолчанию которое mutable
# В данном случае нужно создавать новый список каждый раз при создании нового экземпляра класса,
# иначе все экземпляры класса будут ссылаться на один и тот же список, что неверно

class Person:

    def __init__(self, name: str, surname: str, age: int, books=None):
        if books is None:
            books = []
        self.name = name
        self.surname = surname
        self.age = age
        self.books = books

    def __repr__(self):
        return f"В объекта имеется: {self.__dict__}"

    def __eq__(self, other):
        return self.age == other.age

p1 = Person('Dmitiry', 'Gordeev', 36)
p1.books.append('Python book')
print(p1)

p2 = Person('Sergey', 'Lukianov', 36)
p2.books.append('Java book')
print(p2)

print(p1 == p2)   # True, т.к. им обоим по 36 и метод __eq__ в классе вручную

print("\n_____________________________\n")


# СОЗДАДИМ ДАТА-КЛАСС ДЛЯ УПРОЩЕНИЯ ЗАПИСИ ВЫШЕ


@dataclass
class PersonData:
    name: str
    surname: str
    age: int
    # Используем функцию field() для указания, что в дата-классе будет mutable свойство по-умолчанию
    books: list = field(default_factory=list)

p3 = PersonData('Dmitiry', 'Gordeev', 37)
p3.books.append('Python book')
print(p3)

p4 = PersonData('Sergey', 'Lukianov', 37)
p4.books.append('Java book')
print(p4)

# В дата-классах уже переопределен метод __eq__ и сравниваются значения конкретных свойств или объектов целиком
print(p3.age == p4.age)  # True, т.к. им обоим по 37
