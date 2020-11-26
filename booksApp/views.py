from django.shortcuts import render
from rest_framework.views import APIView
from .serialzer import BookSerializer,BookUpdateSerializer,AuthorUpdateSerializer,AuthorSerializer
from rest_framework.permissions import AllowAny
from basic_curd.constant import  ResponseHandle,PAGE_SIZE
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from .models import Books,Author
from django.urls import reverse, resolve
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator




class BooksCreate(APIView):
    #view to create boook 
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        #handling  exception if any exception occurs in the api
        try:
            serializer = BookSerializer(data=request.data)
            #validating the data recived by serialzier
            if serializer.is_valid(raise_exception=True):
                #query to create to book and only if the data is validated
                Books.objects.create(name=serializer.validated_data['name'],description=serializer.validated_data['description'],
                                        author=Author.objects.get(id=serializer.validated_data['author']),
                                    price=serializer.validated_data['price'],
                                    quantity=serializer.validated_data['quantity'])
                return Response(ResponseHandle.onSuccess(serializer.validated_data), status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(ResponseHandle.onFailure(str(e)))


class BookUpdate(RetrieveUpdateAPIView):
    #view to retrieve and update of books here on the basis of the api request 
    #handling  exception if any exception occurs in the api
    queryset = Books.objects.all()
    serializer_class = BookUpdateSerializer
    lookup_field = 'pk'
    


class BookListing(ListAPIView):
    #view to list the books 
    permission_classes = [AllowAny]
    
    def list(self, request, *args, **kwargs):
        #handling  exception if any exception occurs in the api
        try:
            #checking the query string params and making dict out of it in a filter_parameter and
            #  then using dict unpacking and it itterate over the values to.
            if 'type' in request.query_params  and 'value' in request.query_params:
                filter_parameter = {}
                if 'operator' in request.query_params:
                    filter_parameter[request.query_params['type']+'__'+request.query_params['operator']] = request.query_params['value']
                else:
                    if request.query_params['type'] =='price' or request.query_params['type'] == 'quantity':
                        filter_parameter[request.query_params['type']] = request.query_params['value']
                    elif request.query_params['type'] == 'author':
                        print(request.query_params['type']+'__name__contains')
                        filter_parameter[request.query_params['type']+'__name'] = request.query_params['value']
                    else:
                        filter_parameter[request.query_params['type']+'__contains'] = request.query_params['value']
                queryset = Books.objects.filter(**filter_parameter)
            else:
                queryset = Books.objects.all()

            #pagination logic start
            page = self.request.GET.get('page')
            paginator = Paginator(queryset, PAGE_SIZE)
            try:
                queryset = paginator.page(page)
            except PageNotAnInteger:
                queryset = paginator.page(1)
            except EmptyPage:
                queryset = paginator.page(paginator.num_pages)
            serializer = BookUpdateSerializer(queryset, many=True)
            return Response(ResponseHandle.onSuccess(serializer.data))
        except Exception as e:
            return Response(ResponseHandle.onFailure(str(e)))


class AuthorListing(ListAPIView):
    #view to list author
    permission_classes = [AllowAny]
    
    def list(self, request, *args, **kwargs):
        #handling the exception if any exception occurs in the api
        try:
            #checking the query string params and making dict out of it in a filter_parameter and
            #  then using dict unpacking and it itterate over the values to.
            if 'type' in request.query_params  and 'value' in request.query_params:
                filter_parameter = {}
                if 'operator' in request.query_params:
                    filter_parameter[request.query_params['type']+'__'+request.query_params['operator']] = request.query_params['value']
                else:
                    filter_parameter[request.query_params['type'] + '__contains'] = request.query_params['value']
                queryset = Author.objects.filter(**filter_parameter)
            else:
                queryset = Author.objects.all()
            #pagination logic start
            page = self.request.GET.get('page')
            paginator = Paginator(queryset, PAGE_SIZE)
            try:
                queryset = paginator.page(page)
            except PageNotAnInteger:
                queryset = paginator.page(1)
            except EmptyPage:
                queryset = paginator.page(paginator.num_pages)
            serializer = AuthorUpdateSerializer(queryset, many=True)
            return Response(ResponseHandle.onSuccess(serializer.data))
        except Exception as e:
            return Response(ResponseHandle.onFailure(str(e)))


class AuthorCreate(APIView):
    permission_classes = [AllowAny]
    #view to create author 
    def post(self, request, format='json'):
        # handling exception that may occur
        try:
            serializer = AuthorSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                Author.objects.create(name=serializer.validated_data['name'],username=serializer.validated_data['username'])
                return Response(ResponseHandle.onSuccess(serializer.validated_data), status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(ResponseHandle.onFailure(str(e)))