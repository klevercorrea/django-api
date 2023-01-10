from django.shortcuts import render
from rest_framework import generics
from catalog.models import Book, Author
from catalog.serializers import BookSerializer, AuthorSerializer

# Create your views here.


class BooksViewSet(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BooksDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorsViewSet(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorsDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
