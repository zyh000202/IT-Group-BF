from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from .models import Book, BorrowRecord, Category
from .forms import BookForm

def index(request):
    """Home page: display welcome information and statistics"""
    book_count = Book.objects.count()
    available_count = Book.objects.filter(available_copies__gt=0).count()
    return render(request, 'books/index.html', {
        'book_count': book_count,
        'available_count': available_count,
    })

def book_list(request):
    """Book list, support search"""
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    books = Book.objects.all()
    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)
    if category_id:
        books = books.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, 'books/book_list.html', {
        'books': books,
        'categories': categories,
        'query': query,
        'selected_category': int(category_id) if category_id.isdigit() else '',
    })

def book_detail(request, book_id):
    """Book Details Page"""
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required
def borrow_book(request, book_id):
    """Book borrowing (AJAX supported)"""
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        if not book.is_available():
            return JsonResponse({'success': False, 'message': 'All books have been lent'}, status=400)
        # Check whether the user has borrowed and not returned
        existing = BorrowRecord.objects.filter(user=request.user, book=book, return_date__isnull=True)
        if existing.exists():
            return JsonResponse({'success': False, 'message': 'You have borrowed the book and have not returned it'}, status=400)

        # Create borrowing record
        due = timezone.now() + timezone.timedelta(days=14)  # Default borrowing period is 14 days
        BorrowRecord.objects.create(
            user=request.user,
            book=book,
            due_date=due
        )
        # Reduce the quantity that can be borrowed
        book.available_copies -= 1
        book.save()
        return JsonResponse({'success': True, 'message': 'Borrowing succeeded', 'available': book.available_copies})
    return JsonResponse({'success': False, 'message': 'invalid request'}, status=405)

@login_required
def return_book(request, record_id):
    """Return books (AJAX)"""
    if request.method == 'POST':
        record = get_object_or_404(BorrowRecord, id=record_id, user=request.user, return_date__isnull=True)
        record.return_date = timezone.now()
        record.save()
        # Increase the number of books available for borrowing
        book = record.book
        book.available_copies += 1
        book.save()
        return JsonResponse({'success': True, 'message': 'Return succeeded', 'available': book.available_copies})
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=405)

@login_required
def my_borrows(request):
    """Borrowing record of current user (including history)"""
    current_borrows = BorrowRecord.objects.filter(user=request.user, return_date__isnull=True)
    history = BorrowRecord.objects.filter(user=request.user, return_date__isnull=False)
    return render(request, 'books/my_borrows.html', {
        'current_borrows': current_borrows,
        'history': history,
    })

# Administrator View: Add/Edit/Delete Books
@staff_member_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Book added successfully')
            return redirect('books:book_detail', book_id=book.id)
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form, 'title': 'Add Books'})

@staff_member_required
def book_update(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Books updated successfully')
            return redirect('books:book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form, 'title': 'Edit books'})

@staff_member_required
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully')
        return redirect('books:book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books:index')
    else:
        form = UserCreationForm()
    return render(request, 'books/register.html', {'form': form})