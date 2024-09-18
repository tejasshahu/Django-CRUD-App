from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .forms import BookForm, AuthorForm
from .models import Book, Author


class CreateBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "book_form.html"
    success_url = reverse_lazy('list_books')

class CreateAuthorView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "author_form.html"
    success_url = reverse_lazy('list_books')

class UpdateBookView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "book_form.html"
    success_url = reverse_lazy('list_books')


class DeleteBookView(DeleteView):
    model = Book
    template_name = "book_delete_confirm.html"
    success_url = reverse_lazy('list_books')


class ListBookView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = 'books'

