from django import forms

from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'year_published', 'author']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']