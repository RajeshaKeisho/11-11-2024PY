from django.contrib import admin
from .models import Restaurant, MenuItem, Customer, Order
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Customer)
admin.site.register(Order)