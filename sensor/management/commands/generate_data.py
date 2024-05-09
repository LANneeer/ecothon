from django.core.management.base import BaseCommand

from users.models import User, Car
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()

        # Generate fake data for User
        iin = fake.random_number(digits=12)
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone = fake.phone_number()
        password = fake.password()

        # Create a new User instance
        owner = User.objects.create_user(iin=iin, phone=phone, password=password, first_name=first_name, last_name=last_name)

        # Generate fake data for Car
        gov_reg_sign = fake.license_plate()
        tech_pass = fake.random_number(digits=7)
        date_of_release = fake.date_this_century()
        serial_number = fake.random_number(digits=10)
        body_number = fake.random_number(digits=10)
        frame_number = fake.random_number(digits=10)
        engine_number = fake.random_number(digits=10)
        car_category = fake.random_element(elements=('Sedan', 'SUV', 'Hatchback', 'Convertible'))
        gas_cylinder_number = fake.random_number(digits=10)
        car_number = gov_reg_sign
        car_brand = fake.random_element(elements=('Toyota', 'Honda', 'Ford', 'Chevrolet', 'Hyundai'))

        # Create a new Car instance
        Car.objects.create(
            owner=owner,
            gov_reg_sign=gov_reg_sign,
            tech_pass=tech_pass,
            date_of_release=date_of_release,
            serial_number=serial_number,
            body_number=body_number,
            frame_number=frame_number,
            engine_number=engine_number,
            car_category=car_category,
            gas_cylinder_number=gas_cylinder_number,
            car_number=car_number,
            car_brand=car_brand
        )