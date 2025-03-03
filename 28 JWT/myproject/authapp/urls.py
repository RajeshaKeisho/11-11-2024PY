# authapp/urls.py
from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProtectedView, AdminContentView, ManagerContentView, HRContentView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('protected/', ProtectedView.as_view(), name='protected'),

    path('admin-content/', AdminContentView.as_view(), name='admin_content'),
    path('manager-content/', ManagerContentView.as_view(), name='manager_content'),
    path('hr-content/', HRContentView.as_view(), name='hr_content'),
]





