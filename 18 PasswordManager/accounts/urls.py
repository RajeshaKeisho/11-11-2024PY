from django.urls import path 
from .views import SignUpView, CustomLoginView, HomeView
from django.contrib.auth.views import (
    PasswordChangeView, 
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .views import CustomLogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', CustomLogoutView.as_view(), name='logout_success'),
]