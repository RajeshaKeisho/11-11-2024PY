from django.urls import path 
from . import views

urlpatterns = [
    path("createbook/", views.create_book, name='createbook'),
    path("success/", views.book_success, name='book_success'),
    path("book_list/", views.book_list, name='book_list')
]