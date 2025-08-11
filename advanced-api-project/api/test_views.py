# api/test_views.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = 'testuser'
        self.password = 'testpass'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.author = Author.objects.create(name="Author A")
        self.book = Book.objects.create(title="Book A", publication_year=2020, author=self.author)

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)  # Assuming pagination or list response
        self.assertIsInstance(response.data['results'], list)

    def test_create_book_authenticated(self):
        login = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login, "Login failed in test_create_book_authenticated")
        response = self.client.post('/api/books/', {
            'title': 'Book B',
            'publication_year': 2022,
            'author': self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Book B')
        self.assertEqual(response.data['publication_year'], 2022)
        self.assertEqual(response.data['author'], self.author.id)

    def test_create_book_unauthenticated(self):
        response = self.client.post('/api/books/', {
            'title': 'Book B',
            'publication_year': 2022,
            'author': self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        login = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login, "Login failed in test_update_book")
        response = self.client.put(f'/api/books/{self.book.id}/', {
            'title': 'Updated Book A',
            'publication_year': 2021,
            'author': self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book A')
        self.assertEqual(response.data['publication_year'], 2021)
        self.assertEqual(response.data['author'], self.author.id)

    def test_delete_book(self):
        login = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login, "Login failed in test_delete_book")
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
