from dataclasses import dataclass


@dataclass
class Person:
    firstname: str = None
    lastname: str = None
    middlename: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    num: int = None
