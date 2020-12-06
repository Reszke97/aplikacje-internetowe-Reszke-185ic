from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post
from rest_framework.response import Response


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        #korzystamy z wbudowanego modelu Django dla usera
        model = get_user_model()
        #tutaj podajemy jakie pola chcemy aby nasz plik JSON posiadał
        fields = ('id', 'username',)