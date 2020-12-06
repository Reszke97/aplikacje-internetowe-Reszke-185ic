from django.urls import path
from .views import UserList, UserDetail
#UserViewSet, PostViewSet
from .views import  PostList, PostDetail
from . import views


urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()), 
    path('<int:pk>/', PostDetail.as_view()),
    #path('', views.PostList),
    path('', PostList.as_view()),
    #path('a', views.setcookie, name='test_cookie'),
]
