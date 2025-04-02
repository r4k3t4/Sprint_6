import faker
import random


def reg_new_user():
    fake = faker.Faker("ru_RU")
    firstname = fake.first_name()
    lastname = fake.last_name()
    address = fake.city()
    email = fake.email()
    password = fake.password()
    return firstname, lastname, address, email, password


def telephone_number():
    number = random.randint(80000000000, 89999999999)
    return number
