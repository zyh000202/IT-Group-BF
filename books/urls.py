from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/<int:book_id>/borrow/', views.borrow_book, name='borrow_book'),
    path('records/<int:record_id>/return/', views.return_book, name='return_book'),
    path('my-borrows/', views.my_borrows, name='my_borrows'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:book_id>/update/', views.book_update, name='book_update'),
    path('books/<int:book_id>/delete/', views.book_delete, name='book_delete'),
    path('register/', views.register, name='register'),
]