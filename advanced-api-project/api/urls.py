from django.urls import path
from .views import BookCreateView, BookDeleteView, BookDetailView, BookListView, BookUpdateView, AuthorListView

urlpatterns = [
    path('books/list-books/', BookListView.as_view(), name='list_books' ),
    path('books/retrieve-book/<int:pk>/', BookDetailView.as_view, name='retrieve_book' ),
    path('books/create-book/', BookCreateView.as_view(), name='create_book' ),
    path('books/update-book/', BookUpdateView.as_view(), name='update_book' ),
    path('books/delete-book/<int:pk>', BookDeleteView.as_view(), name='delete_book' ),
    path('authors/create/', AuthorListView.as_view(), name='delete_book' ),
]

