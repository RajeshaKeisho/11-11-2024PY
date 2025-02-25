from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.contrib import admin
from delivery.views import RestaurantViewSet, MenuItemViewSet, CustomerViewSet, OrderViewSet, CategoryViewSet, DeliveryDriverViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
# Set up the DefaultRouter and register viewsets
router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

router.register(r'categories', CategoryViewSet)
router.register(r'drivers', DeliveryDriverViewSet)

# Define the URL patterns for both the API and the admin interface
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface URL
    path('api/', include(router.urls)),  # API endpoints for the app
    path('apiapp/', include('delivery.urls')),  
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]

