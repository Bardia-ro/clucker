
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
import faker

from microblogs.models import User


class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')


    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(0,100):
            User.objects.create_user(
                username = fake.user_name(),
                first_name =  fake.first_name(),
                last_name = fake.last_name(),
                email = fake.email(),
                password = fake.password(),
                bio = fake.paragraph()      
        )
