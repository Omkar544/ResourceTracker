from django.contrib import admin
# Import the necessary Admin class for custom users
from django.contrib.auth.admin import UserAdmin 
# Import get_user_model from the correct location
from django.contrib.auth import get_user_model 
from .models import Employee

# 1. Unregister the default User model using the correctly imported function
try:
    admin.site.unregister(get_user_model())
except admin.sites.NotRegistered:
    # Handle the case where the default user model might not be registered yet
    pass

# 2. Register your Custom Employee model with the standard UserAdmin features
admin.site.register(Employee, UserAdmin)