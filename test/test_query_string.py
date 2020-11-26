# import pytest
# from rest_framework.test import APITestCase
# from parameterized import parameterized
# from rest_framework import status
# from booksApp.models import Author



# test_value = [('author1','author_u1','book1','description1',2,2),('author2','author_u2','book2','description2',2,2)]

# class Testingt_Views(APITestCase):
#     @parameterized.expand(test_value)
#     def test_book_detail(self,author_name,author_username,book_name,description,price,quantity):
        # author_obj = Author.objects.create(name=author_name,username=author_username)
        # data = {"name":book_name,"author":author_obj.id,"description":description,"price":price,"quantity":quantity}
        # response  =  self.client.post(reverse('books_create'), data)
        # # response = self.client.get(reverse('books_update',kwargs={'pk':author_obj.id}))
        # self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        # self.assertEqual(response.data['name'],book_name)