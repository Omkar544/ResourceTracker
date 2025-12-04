from django.urls import path
from . import views

urlpatterns = [
    # This maps the root path of the project to your test view
    path('', views.test_config_view, name='test_home'),
]