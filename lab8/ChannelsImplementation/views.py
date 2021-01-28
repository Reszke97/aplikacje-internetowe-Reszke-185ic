# chat/views.py
from django.shortcuts import render

def create_room(request):
    return render(request, 'chat/create_room.html')

def chat_room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})

def home(request):
    return render(request,'chat/home.html')

def fibonacci(request):
    return render(request,'chat/fibonacci.html')

def factorial(request):
    return render(request,'chat/factorial.html')