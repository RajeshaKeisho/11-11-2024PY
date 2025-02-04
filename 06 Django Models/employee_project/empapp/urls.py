from django.urls import path 
from .views import employee_view

urlpatterns = [
    path("employees/", employee_view, name='employees'),
]