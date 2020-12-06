from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import UserViewSet, BookViewSet


#teraz zamiast podawać urlpatterns korzystamy z Routerów.
#Routery działają bezpośrednio na zbiorach widoków(viewsets).
#Automatycznie generują za nas adresy URL.

#stworzenie nowego Routera(obiektu klasy Router)
router = SimpleRouter()

#przekazanie do naszego nowo utowrzonego Routera wcześniej utworzonych viewsetów
#podajemu mu równierz jak ma nazywać się początek scieżki
router.register('users', UserViewSet, basename='users')
router.register('', BookViewSet, basename='books')

#na koniec wywoływana metoda która tworzy za nas gotowy urlpatterns
urlpatterns = router.urls