from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.contrib import admin
from delivery.views import RestaurantViewSet, MenuItemViewSet, CustomerViewSet, OrderViewSet

# Set up the DefaultRouter and register viewsets
router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

# Define the URL patterns for both the API and the admin interface
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface URL
    path('api/', include(router.urls)),  # API endpoints for the app
]
