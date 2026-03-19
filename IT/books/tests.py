from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Book, Category, BorrowRecord

class BookModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.book = Book.objects.create(
            title='Test Book',
            author='Author',
            isbn='1234567890123',
            category=self.category,
            total_copies=5,
            available_copies=5
        )

    def test_is_available_true(self):
        self.assertTrue(self.book.is_available())

    def test_is_available_false(self):
        self.book.available_copies = 0
        self.book.save()
        self.assertFalse(self.book.is_available())

class BorrowViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Fiction')
        self.book = Book.objects.create(
            title='Django Guide',
            author='Me',
            isbn='9876543210123',
            category=self.category,
            total_copies=2,
            available_copies=2
        )

    def test_borrow_book_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(f'/books/{self.book.id}/borrow/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])
        self.assertEqual(BorrowRecord.objects.count(), 1)
        self.book.refresh_from_db()
        self.assertEqual(self.book.available_copies, 1)

    def test_borrow_book_unauthenticated(self):
        response = self.client.post(f'/books/{self.book.id}/borrow/')

        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)