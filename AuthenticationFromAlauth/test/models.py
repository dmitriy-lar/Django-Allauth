from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

    