import pytest
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from booksApp.models import Author,Books
from parameterized import parameterized
import json


test_value = [('author1','author_u1','book1','description1',2,2),('author2','author_u2','book2','description2',20,21),
              ('author3','author_u3','book3','description1',20,22),('author4','author_u4','book4','description4',12,13),  ]

negative_test_case_for_create_book = [ {"author":1,"description":"hello","price":2,"quantity":2},
                            {"name":"my life in red corner","description":"hello","price":2,"quantity":2},
                            {"name":"my life in red corner","author":1,"price":2,"quantity":2},
                            {"name":"my life in red corner","author":1,"description":"hello","price":2},
                            {"name":"my life in red corner","author":1,"description":"hello","quantity":2},
                            {"description":"hello","price":2,"quantity":2}]


class Testingt_Views(APITestCase):
    def test_create_books(self):
        author_obj = Author.objects.create(name='test',username='test')
        data = {"name":"my life in red and white","author":author_obj.id,"description":"hello","price":2,"quantity":2}
        response  =  self.client.post(reverse('books_create'), data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_case_for_negative_create_books(self):
        for item in negative_test_case_for_create_book:
            author_obj = Author.objects.create(name='test',username='test_1')
            if 'author' in item:
                item['author'] = author_obj.id
                response  =  self.client.post(reverse('books_create'), item)
                self.assertEqual(response.status_code,status.HTTP_200_OK)
            else:
                response  =  self.client.post(reverse('books_create'), item)
                self.assertEqual(response.status_code,status.HTTP_200_OK)



    
    @parameterized.expand(test_value)
    def test_book_detail(self,author_name,author_username,book_name,description,price,quantity):
        author_obj = Author.objects.create(name=author_name,username=author_username)
        Books.objects.create(name=book_name, author=  author_obj,description=description,
                                price=price,
                                quantity=quantity)
        response = self.client.get(reverse('books_update',kwargs={'pk':author_obj.id}))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['name'],book_name)

    def test_book_list(self):
        response  =  self.client.get(reverse('books_list'))
        assert response.status_code == status.HTTP_200_OK
    
    def test_query_params(self):
        for item in test_value:
            author_obj = Author.objects.create(name=item[0],username=item[1])
            Books.objects.create(name=item[2], author=  author_obj,description=item[3],
                                price=item[4],
                                quantity=item[5])
        response = self.client.get('/get/books',{'type':'price','value':'20'})
        response1 = self.client.get('/get/books',{'type':'price','value':'2','operator':'gte'})
        self.assertEqual(len(response.data['data']), 2)
        
        self.assertEqual(len(response1.data['data']),4)
