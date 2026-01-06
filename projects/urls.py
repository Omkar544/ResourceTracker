from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # ADD THIS LINE BELOW:
    path('log-time/', views.log_time, name='log_time'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]   