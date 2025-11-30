from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    def setUp(self):
    # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
    
    # Log in the test client
        self.client.login(username='testuser', password='testpass')
    
    # Sample books
        Book.objects.create(title="Harry Potter", author="J.K. Rowling", publication_year=1997)
        Book.objects.create(title="Animal Farm", author="George Orwell", publication_year=1945)

    def test_list_books(self):
        url = reverse('book-list')  # Make sure your URL name matches
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # We created 3 books

    def test_retrieve_book(self):
        book = Book.objects.first()
        url = reverse('book-detail', args=[book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], book.title)
    def test_create_book(self):
        url = reverse('book-list')
        data = {'title': 'Django for APIs', 'author': 'William S. Vincent', 'publication_year': 2020}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_update_book(self):
        book = Book.objects.first()
        url = reverse('book-detail', args=[book.id])
        data = {'title': 'Harry Potter Updated', 'author': book.author, 'publication_year': book.publication_year}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, 'Harry Potter Updated')

    def test_delete_book(self):
        book = Book.objects.first()
        url = reverse('book-detail', args=[book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)
    def test_filter_books_by_author(self):
        url = reverse('book-list')
        response = self.client.get(url, {'author': 'George Orwell'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_books_by_title(self):
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Harry'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year_desc(self):
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1997)  # Harry Potter    