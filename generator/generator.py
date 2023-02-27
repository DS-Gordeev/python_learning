from autotests_python.data.data import Person
from faker import Faker
from random import randint
fakre_ru = Faker('ru_RU')


def genereted_person():
    yield Person(
        firstname=fakre_ru.first_name(),
        lastname=fakre_ru.last_name(),
        middlename=fakre_ru.middle_name(),
        email=fakre_ru.email(),
        current_address=fakre_ru.address(),
        permanent_address=fakre_ru.address(),
        num=randint(1, 10),
    )

person_info = next(genereted_person())
print(person_info.email)

