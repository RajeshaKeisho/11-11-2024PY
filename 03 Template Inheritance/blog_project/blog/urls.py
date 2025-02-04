from django.urls import path 
from . import views
urlpatterns = [
   path('home/', views.home), 
   path('about/', views.about), 
   path('contacts/', views.conatcts), 
   path('services/', views.services), 
]