from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    age = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.username