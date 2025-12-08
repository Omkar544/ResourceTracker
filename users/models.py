from django.db import models
from django.contrib.auth.models import AbstractUser

class Employee(AbstractUser):
    # ... (rest of your custom fields like designation, is_manager, etc.)
    pass