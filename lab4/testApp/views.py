from django.shortcuts import render
from django.contrib.auth import get_user_model 
from rest_framework import filters

from rest_framework import viewsets
from rest_framework import generics, permissions
from .models import Book

from .permissions import IsAuthorOrReadOnly
from .serializers import BookSerializer, UserSerializer
# Create your views here.

class BookList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,) # View-Level Permissions
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # Dodałem wyszukiwanie po tytule i filtrowanie również, ponieważ był problem z kluczem obcym
    search_fields = ['title']
    ordering_fields = ['title']

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer