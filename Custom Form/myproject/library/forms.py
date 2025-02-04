from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']

        widgets = {
            'title':forms.TextInput(attrs={'class':"form-control", 'placeholder':"Book Title"}),
            'author':forms.TextInput(attrs={'class':"form-control", 'placeholder':"Author"}),
            'published_date':forms.DateInput(attrs={'class':"form-control", 'placeholder':"YYYY-MM-DD"}),
            'isbn':forms.TextInput(attrs={'class':"form-control", 'placeholder':"ISBN"})
        }

        error_message = {
            'title': {
                'required':"Please enter the book title"
            },
            'author':{
                'required':"Please enter the Author name"
            },

            'published_date':{
                'required':"Please enter the publication date",
                'invalid':"Please enter a valid format(YYYY-MM-DD)"
            },
            'isbn':{
                'required':"Please enter the ISBN Number",
                'invalid':"A book with this ISBN already exist"
            },

        }

    def clean_isbn(self):
        isbn = self.cleaned_data.get("isbn")
        if len(isbn) != 13:
            raise forms.ValidationError("ISBN must be 13 Characters long.")
        return isbn