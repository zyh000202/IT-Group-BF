from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Book, BorrowRecord

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'isbn', 'category', 'total_copies', 'available_copies')
    list_filter = ('category',)
    search_fields = ('title', 'author', 'isbn')

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'borrow_date', 'due_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('user__username', 'book__title')