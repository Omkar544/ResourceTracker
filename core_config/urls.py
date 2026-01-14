from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Import Django's auth views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Add this line for the default login page
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    
    # 2. Add this line for the logout page
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Your existing projects URLs
    path('', include('projects.urls')),
]