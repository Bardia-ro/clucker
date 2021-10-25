from django.core.management.base import BaseCommand, CommandError
from django.db.models.query import InstanceCheckMeta
from microblogs.models import User

class Command(BaseCommand):

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        m=0
        for i in range(User.objects.all().count()):
            if not User.objects.all()[m].is_superuser:
                user = User.objects.all()[m]
                user.delete()
            else:
                m=m+1

         


                
                    