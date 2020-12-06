from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model 

from rest_framework import viewsets
from rest_framework import generics, permissions
from .models import Post

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import HTMLFormRenderer,JSONRenderer,BrowsableAPIRenderer 

class PostList(APIView):
    serializer_class = PostSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)


    # Nalezy zdefiniować metode POST bez niej nie wyświetli się formularz z postem
    def post(self, request, *args, **kwargs):

        #Przekazujemy nasze dane z Serializera
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            #Zapisujemy serializer a następnie zwracamy dane
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Należy też zdefiniować metodę GET bez niej nie wyświetli się nasze dane
    def get(self, request, *args, **kwargs):
        snippets = Post.objects.all()
        serializer = PostSerializer(snippets,many=True)

        #Tworzymy nowy obiekt klasy respone i przekazujemy do niego serialize a później
        #Tworzymy nowy cookie do tego obiektu
        html = Response(serializer.data)
        # Jeśli cookie jest już istnieje to wykona się if
        if request.COOKIES.get('visits'):
            #do cookie dataflair dodajemy String o nazwie Witaj z powrotem!
            html.set_cookie('dataflair', 'Witaj z powrotem!')
            #pobieramy wartość ze zmiennej visits jako liczba całkowita
            value = int(request.COOKIES.get('visits'))
            #Do zmiennej visits dodajemy 1
            html.set_cookie('visits', value + 1)
            return html
        else:
            value = 1
            text = "Witaj po raz 1!"
            html.set_cookie('visits', value)
            html.set_cookie('dataflair', text)
            return html

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer