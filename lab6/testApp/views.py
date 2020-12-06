from django.shortcuts import render
from django.contrib.auth import get_user_model 
from rest_framework import filters

from rest_framework import viewsets
from rest_framework import generics, permissions
from .models import Book

from .permissions import IsAuthorOrReadOnly
from .serializers import BookSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

#zamiast tworzyć 2 osobne klasy dla wyświetlenia wszystkich postów
#oraz wyświetlenia postów osobno tworzymy jedną klasę
#korzystając z viewsets.ModelViewSet
#nie trzeba podawać scieżek w url patterns
#ale należy skorzystać z Router'ów
#dzięki temu jest mniej wymaganych linii kodu


class BookViewSet(viewsets.ModelViewSet): 
    permission_classes = (IsAuthorOrReadOnly,IsAuthenticated)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # Dodałem wyszukiwanie po tytule i filtrowanie również, ponieważ był problem z kluczem obcym
    search_fields = ['title']
    ordering_fields = ['title']

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer