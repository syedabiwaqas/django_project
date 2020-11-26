
from django.contrib import admin
from django.urls import path
from booksApp.views import BooksCreate,BookUpdate, BookListing, AuthorListing, AuthorCreate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/book', BooksCreate.as_view(),name='books_create'),
    path('get/book/<int:pk>', BookUpdate.as_view(),name='books_update'),
    path('get/books', BookListing.as_view(),name='books_list'),
    path('get/authors', AuthorListing.as_view(),name='author_list'),
    path('post/author', AuthorCreate.as_view(),name='author_create'),
]
