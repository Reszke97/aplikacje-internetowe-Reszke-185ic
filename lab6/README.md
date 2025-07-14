# Lab 6 – Zezwolenia i uwierzytelnianie w DRF

## Źródło
🔗 https://zacniewski.gitlab.io/teaching/2020-internet-apps/lab06/


# Zadanie zostało wykonane na istniejących już aplikacjach z laboratorium nr 4. Dodane zostały viewsety, routery, uwierzytelnianie oraz licznik wizyt z użyciem cookies. Zapoznanie dokumentacji przy dokonywaniu modyfikacji jest konieczne przy jakich kolwiek większych zmianach.

# Aplikacja Post(api v1):
### Dodany został widok dla logowania/wylogowania, resetu hasła/potwierdzeniu resetu hasła dzięki pakietowi **Django-rest-auth**, który należy pobrać a następnie w pliku **settings.py** w **installed_apps** dodajemy **'rest_framework.authtoken'** a w plikach url blog_api_project należy dodać 2 scieżki:
- path('api/v1/rest-auth/', include('rest_auth.urls')),
- path('api/v2/rest-auth/registration/', include('rest_auth.registration.urls')),

### Tak przedstawia się widok logowania:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/1.PNG)

### Tak przedstawia się widok logout:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/2.PNG)

### Tak przedstawia się widok Password Reset:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/3.PNG)

### Tak przedstawia się widok Password Confirm:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/4.PNG)

### Dodany został również widok rejestracji dzięki pakietowi **Django-allauth**. Należy go zainstalować, następnie w pliku **settings.py** w **installed_apps** dodać:

- 'django.contrib.sites',

- 'allauth', 

- 'allauth.account', 

- 'allauth.socialaccount', 

- 'rest_auth.registration'

oraz poza **installed_apps** dodać: **EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'** oraz **SITE_ID = 1**

### Tak przedstawia się widok **rejestracji**
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/5.PNG)


### Po zarejstrowaniu w panelu administratora pojawi się nam użytkownik:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/6.PNG)

### Pojawił się również token przypisany do użytkownika:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/7.PNG)

## Uwierzytelnianie w DRF posiada 2 domyślne metody: **SessionAuthentication** oraz **BasicAuthentication**, których nawet nie trzeba wpisywać w **'Default Authentication'**. Aby uruchomić uwierzytelnianie za pomocą tokenu należy dodać do **'DefaultAuthentication'** **TokenAuthentication**. Można połączyć uwierzytelnianie za pomocą tokenu i sesji co pokazuje rysunek poniżej:

![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/8.PNG)

### Jak widać gdy uwierzytelnianie dla sesji jest włączone to użytkownik bez tokenu również jest w stanie się zalogować.
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/9.PNG)

### Jednak gdy zostawimy włączone uwierzytelnianie tylko za pomocą tokenu:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/11.PNG)

### Użtkownik bez tokenu nie będzie mógł się zalogować:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/10.PNG)

## Został utworzony również widok, który wyświetla wszystkich zarejstrowanych użytkowników:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/12.PNG)

## Dodany również został prosty licznik wizyt z użyciem ciasteczek. Do stworzenia licznika w naszym API niezbędne było zaznajomienie się z dokumentacją DRF a konkretnie https://www.django-rest-framework.org/tutorial/3-class-based-views/ . W widokach należalo utworzyć nową klasę **PostList** jako **APIView** i zaimportować:

- **from rest_framework.response import Response**

- **from rest_framework.views import APIView**

- **from rest_framework import status**

- **from rest_framework.renderers import HTMLFormRenderer,JSONRenderer,BrowsableAPIRenderer**

## Następnie użyć stworzonego wcześniej serializera i przekazać go do **serializer_class** oraz podać **renderer_classes** z importa. Po czym zaimplementować wbudowaną metodę dla **GET** i **POST**. W metodzie GET tworzymy ciasteczko i pobieramy dane z bazy danych. Przy metodzie Post pobieramy model tabelki bazy danych do forma, wyświetlamy go oraz należy zdefiniować opcję **save**. W ciasteczkach utworzone 2 zmienne:
- **visits** określająca ile razy użytkownik odwiedził stronę.
- **dataflair** zawierający string z informacją.

## Tworzenie ciasteczek:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/20.PNG)

## Aby wyświetlić cookies w Google Chrome należy wejść w developer tools i następnie wybrać zakładkę Application.

### Gdy użytkownik odwiedzi strone po raz pierwszy to pokaże mu się napis "witaj po raz 1!" oraz zmienna visits=1:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/13.PNG)

### Gdy użytkownik odwiedzi strone po raz kolejny to pokaże mu się napis "witaj z powrotem! oraz zmienna visits=2"
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/14.PNG)

# Aplikacja testApp(api v2)

## Dodany tutaj został **viewsets** oraz **routery** oraz niezbędne było zmodyfikowanie permisson classes gdyż we viewsetach nie jest czytane **defaultpermission z pliku settings**.

## Zamiast tworzyć 2 osobne klasy dla wyświetlenia wszystkich postów oraz wyświetlenia postów osobno tworzymy jedną klasę korzystając z viewsets.ModelViewSet nie trzeba podawać scieżek w url patterns ale należy skorzystać z Router'ów dzięki temu jest mniej wymaganych linii kodu. Teraz w pliku view należy dodatkowo do zmiennej **permission_classes** dodać isAuthenticated oraz zaimportować **from rest_framework.permissions import IsAuthenticated** 
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/18.PNG)

## Tak musi wyglądać zmienna permisison_classes po zmianach:**permission_classes = (IsAuthorOrReadOnly,IsAuthenticated)**.

### Teraz gdy użytkownik nie będzie zalogowany to nie będzie w stanie wyświetlić danych:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/16.PNG)

### Tak przedstawia się widok BookViewSet:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/15.PNG)

### Tak przedstawia się widok UserViewSet:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/19.PNG)

## W pliku **urls.py** należy stworzyć nowy obiekt klasy router. Stworzony został SimpleRouter(). Następnie za pomocą obiektu tworzymy nowe scieżki za pomocą metody register() i przekazujemy tam jak ma nazywać się początek naszej scieżki i ViewSet. Po czym przekazujemy do urlpatterns nowo wygenerowane scieżki.
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab6/zrzuty/17.PNG)



