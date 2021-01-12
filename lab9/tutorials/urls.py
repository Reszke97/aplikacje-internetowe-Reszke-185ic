from django.conf.urls import url 
from tutorials import views 
from django.urls import path
from .views import PostDetail
urlpatterns = [ 
    path('api/tutorials', views.PostView.as_view(), name= 'posts_list'),
    path('api/tutorials/<int:pk>/', PostDetail.as_view()),
]