# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class Employee(AbstractUser):
    """
    Extends the default Django User to include corporate fields.
    """
    DESIGNATION_CHOICES = [
        ('DEV', 'Developer'),
        ('QA', 'Quality Analyst'),
        ('MAN', 'Manager'),
        ('TRAINEE', 'Trainee'),
    ]
    
    designation = models.CharField(
        max_length=10, 
        choices=DESIGNATION_CHOICES, 
        default='TRAINEE'
    )
    department = models.CharField(max_length=100, blank=True)
    is_manager = models.BooleanField(default=False, 
                                     help_text="Designates whether this user is a project manager.")
    
    # Simple skill tracking field
    skills = models.CharField(max_length=255, help_text="Comma-separated skills (e.g., Python, SQL, Testing)", blank=True)

    def __str__(self):
        # Fallback to username if name fields are empty
        return f"{self.first_name} {self.last_name or self.username} ({self.designation})"