from data import Person
from faker import Faker
from random import randint


faked = Faker('ru_RU')
Faker.seed()


def genereted_person():
    yield Person(
        firstname=faked.first_name(),
        lastname=faked.last_name(),
        middlename=faked.middle_name(),
        email=faked.email(),
        current_address=faked.address(),
        permanent_address=faked.address(),
        num=randint(1, 10),
    )

person_info = next(genereted_person())
print(person_info.email)


