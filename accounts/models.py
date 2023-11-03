from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4 as v4


class Account(AbstractUser):
    id = models.UUIDField(default=v4, editable=False, primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128, blank=False, null=False)
    is_superuser = models.BooleanField(default=False, null=True)
