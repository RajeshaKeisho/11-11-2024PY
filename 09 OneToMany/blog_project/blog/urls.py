from django.urls import path 
from .views import AuthorListView, AuthorDetailView, BookListView, BooksDeatilView
urlpatterns = [
    path("authors/", AuthorListView.as_view(), name='author-list'),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name='author-detail'),
    path("books/", BookListView.as_view(), name='book-list'),
    path("books/<int:pk>/", BooksDeatilView.as_view(), name='book-detail')
]