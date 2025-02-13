from django.contrib import admin
from django.urls import path, include
from accounts.views import CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout_success/', CustomLogoutView.as_view(), name='logout_success'),
]
