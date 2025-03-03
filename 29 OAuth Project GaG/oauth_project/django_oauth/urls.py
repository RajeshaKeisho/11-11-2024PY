# django_oauth/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('oauth/', include('social_django.urls', namespace='social')),  # OAuth URLs
]
