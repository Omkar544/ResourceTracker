from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('log-time/', views.log_time, name='log_time'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/<int:project_id>/export/', views.export_timesheets_csv, name='export_csv'),
    
    # --- ADD THIS LINE FOR DAY 10 ---
    path('profile/', views.profile_view, name='profile'), 
]