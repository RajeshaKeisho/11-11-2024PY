from django.urls import path 

from . import views

urlpatterns = [
    path("employees/", views.EmployeeListView.as_view(), name='employees'),
    path("customers/", views.CustomerListView.as_view(), name='customers'),
]