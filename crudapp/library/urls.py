from django.urls import path
from .views import (ListBookView, CreateBookView, UpdateBookView,
                    DeleteBookView, CreateAuthorView)


urlpatterns = [
    path('', ListBookView.as_view(), name='list_books'),
    path('create/', CreateBookView.as_view(), name='create_book'),
    path('create_author/', CreateAuthorView.as_view(), name='create_author'),
    path('update/<int:pk>/', UpdateBookView.as_view(), name='update_book'),
    path('delete/<int:pk>/', DeleteBookView.as_view(), name='delete_book')
]

