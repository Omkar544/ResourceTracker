from django.db import models
from users.models import Employee 

class Client(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='managed_projects')
    start_date = models.DateField()
    deadline = models.DateField()
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return self.name

class Timesheet(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='timesheets')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='timesheets')
    date = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'project', 'date')

    def __str__(self):
        return f"{self.employee.username} - {self.project.name} - {self.date}"