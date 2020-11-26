import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from booksApp.models import Books,Author
from booksApp.serialzer import BookSerializer, BookUpdateSerializer

class CreateBookTestCase(APITestCase):
    def test_add_book(self):
        author_obj = Author.objects.create(name='test',username='test')
        data = {"name":"book1","author":author_obj,"description":"hello","price":2,"quantity":2}

        response = self.client.post(reverse('books_create'),data)
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)

    def test_book_detail(self):
        Books.objects.create(name='book1',description='hello',
                                price=2,
                                quantity=2)
        response = self.client.get(reverse('books_update',kwargs={'pk':1}))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['name'],'book1')
    
    # def test_book_update(self):
    #     # Books.objects.create(name='book1',description='hello',
    #     #                         price=2,
    #     #                         quantity=2)
    #     response = self.client.patch(reverse('books_update',kwargs={'pk':1}),{'name':'Abi'})
    #     self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    #     self.assertEqual(response.data['name'],'book1')