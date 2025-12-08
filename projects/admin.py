from django.contrib import admin
# This import should now work correctly after models.py is fixed
from .models import Client, Project 

# Register your models here.
admin.site.register(Client)
admin.site.register(Project)