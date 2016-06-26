from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    phonenumber=models.CharField(
            max_length=10,
            blank=True,
            null=True,
    )
    

