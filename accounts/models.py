from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128, blank=False, null=False)
    is_superuser = models.BooleanField(default=False, null=True)
