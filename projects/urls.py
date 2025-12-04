from django.urls import path
from . import views

urlpatterns = [
    # Map the root path of the app (which will be the project root for now) to the test view
    path('', views.test_config_view, name='test_home'),
]