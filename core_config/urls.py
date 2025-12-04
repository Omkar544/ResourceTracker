from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line tells Django to send all remaining traffic to your projects app
    path('', include('projects.urls')), 
]