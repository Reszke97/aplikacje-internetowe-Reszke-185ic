# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('chat/', views.create_room, name='index'),
    path('chat/<str:room_name>/', views.chat_room, name='room'),#tutaj po chat/ z szablonu gdzie podajemy roomName 
                                                                #jest on tu przekazywany i następnie zwracany w slowniku we viewsach wazne zeby zmienna tutaj po str: miala taka sama
                                                                # nazwe jak tak we viewsach w zwracanym slowniku inaczej serwer nie bedzie wiedzial na jakim kanale jestesmy
    path('',views.home, name='home'),
    path('fibonacci/',views.fibonacci, name='web_workers'),
    path('factorial/',views.factorial, name='factorial'),
]