from faker import Faker

fake = Faker()


def modelUser():
    name = fake.name()
    last_name = fake.last_name()

    return {
        "id": fake.uuid4(),
        "name": name,
        "lastName": last_name,
        "email": f"{name}.{last_name}@{fake.domain_name()}".replace(" ", ""),
        "password": fake.password(),
    }
