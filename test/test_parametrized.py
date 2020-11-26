import pytest
# from booksApp.views import add

test_value = [(7,3,10),('hello',' world','hello world'),(10.3,7.5,17.8)]

@pytest.mark.parametrize('x,y,result' ,test_value)
def test_add(x,y, result):
    assert x+y ==  result