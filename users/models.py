from django.db import models
from django.contrib.auth.models import AbstractUser

class Employee(AbstractUser):
    # Updated to allow empty values for easier admin creation
    designation = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username