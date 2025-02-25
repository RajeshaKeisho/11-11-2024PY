from rest_framework import viewsets
from .models import Restaurant, MenuItem, Customer, Order, Category, DeliveryDriver
from .serializers import RestaurantSerializer, MenuItemSerializer, CustomerSerializer, OrderSerializer, CategorySerializer, DeliveryDriverSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# ------------------------------------------------------------------

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DeliveryDriverViewSet(viewsets.ModelViewSet):
    queryset = DeliveryDriver.objects.all()
    serializer_class = DeliveryDriverSerializer



from django.shortcuts import render
from .models import Restaurant

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants.html', {'restaurants': restaurants})


from django.shortcuts import render
from .models import MenuItem

def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu_items.html', {'menu_items': menu_items})

from django.shortcuts import render
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})


from django.shortcuts import render
from .models import Order

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})
