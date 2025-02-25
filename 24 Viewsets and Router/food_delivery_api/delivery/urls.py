from django.urls import path
from .views import restaurant_list, menu_list, customer_list, order_list

urlpatterns = [
    path('restaurants/', restaurant_list, name='restaurant-list'),
    path('menu-items/', menu_list, name='menuitem-list'),
    path('customers/', customer_list, name='customer-list'),
    path('orders/', order_list, name='order-list'),
]
