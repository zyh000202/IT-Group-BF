from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    """Book category"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Book information"""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    total_copies = models.PositiveIntegerField('total copies', default=1)
    available_copies = models.PositiveIntegerField('available copies', default=1)
    description = models.TextField(blank=True)
    published_date = models.DateField(null=True, blank=True)
    cover_image = models.URLField(blank=True, help_text='Cover image URL')

    def __str__(self):
        return f"{self.title} by {self.author}"

    def is_available(self):
        """Check if there are copies available for borrowing"""
        return self.available_copies > 0

class BorrowRecord(models.Model):
    """Borrowing record"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrow_records')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_records')
    borrow_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-borrow_date']

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

    def is_overdue(self):
        """Check if the book is overdue"""
        if self.return_date:
            return False
        return timezone.now() > self.due_date