from django.contrib import admin
from .models import Client, Project, Timesheet

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'contact_email')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'manager', 'status', 'deadline')
    list_filter = ('status', 'client')

@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    list_display = ('employee', 'project', 'date', 'hours_worked')
    list_filter = ('date', 'project', 'employee')