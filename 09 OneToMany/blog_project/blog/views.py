from django.shortcuts import render
from .models import Author, Books 
from django.views.generic import ListView, DetailView


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'

class BookListView(ListView):
    model = Books
    template_name = 'books_list.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'  

class BooksDeatilView(DetailView):
    model = Books
    template_name = 'book_detail.html'   

