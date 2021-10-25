from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.lookups import Regex

# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        blank=False,
        max_length=30,
        unique = True,
        validators=[RegexValidator(
            regex=r'^@\w{3,}$',
            message='username must consist of @ followed by at least 3 alphanumerical'
        )]

    )

    first_name = models.CharField(unique=False, max_length=50, blank=False)
    last_name = models.CharField(unique=False, max_length=50, blank=False)
    email = models.EmailField(max_length=50, unique=True, blank=False)
    bio = models.TextField()
