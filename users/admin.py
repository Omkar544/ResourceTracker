# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Employee

# Get the default User model
User = get_user_model()

# 1. Unregister the default User model if it exists in the Admin site
if admin.site.is_registered(User):
    admin.site.unregister(User)

# 2. Register your Custom Employee model using the standard UserAdmin class
@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    # This ensures your custom fields (if any) and the UserAdmin fields are used.
    pass