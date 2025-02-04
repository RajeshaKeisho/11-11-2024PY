from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_success")
    else:
        form = BookForm()
    return render(request, 'library/create_book.html', {'form':form})

def book_success(request):
    return render(request, 'library/success.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books':books})
