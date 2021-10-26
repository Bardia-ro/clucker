from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
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


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=True)
    text = models.TextField(max_length=280,unique=False,blank=False)
    created_at = models.DateField(auto_now_add=True, blank=True, editable=False)
    