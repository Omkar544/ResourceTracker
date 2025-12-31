from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # ADD THIS LINE BELOW:
    path('log-time/', views.log_time, name='log_time'),
]