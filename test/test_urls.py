import pytest
from django.urls import reverse,resolve

test_value=[('books_create','BooksCreate'),
            ('books_update','BookUpdate'),
            ('books_list','BookListing'),
            ('author_list','AuthorListing'),
            ('author_create','AuthorCreate')]

            
class Test_Urls:
    @pytest.mark.parametrize('url_name,function_name' ,test_value)
    def test_urls(self,url_name,function_name):
        if url_name == 'books_update':
            func = resolve(reverse(url_name, kwargs={'pk': 1})).func
        else:
            func = resolve(reverse(url_name)).func
        assert func.__name__ ==  function_name

    