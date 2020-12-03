from django.urls import path
from .views import  BookList, BookDetail

urlpatterns = [
    # path('users/', UserList.as_view()),
    # path('users/<int:pk>/', UserDetail.as_view()), 

    path('<int:pk>/', BookDetail.as_view()),
    path('', BookList.as_view()),
]