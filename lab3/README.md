# Aplikacja została utworzona na serwerze Heroku.
# Link do strony na serwerze heroku:https://mareszkeblog.herokuapp.com/
Do zaimplementowania mechanizmu uwierzytelniniania użytkownika za pomocą aplikacji społecznościowych zastosowałem pakietu **django-allauth**. Korzystanie z pakietu **Django-allauth** jest przyjemne dla programisty ponieważ daje on dużo możliowści a przede wszystkim jest prosty w obsłudze i można korzystać z gotowych szablonów i widoków. W dokumentacji jest wszystko opisane a zmiany wymagają tylko kilku zmian w kodzie. Oczywiście można edytować lub dodawać swoje formularze czy szablony w zależności od potrzeb. Ja skorzystałem z prostej metody uwierzytelniania, która nie wymaga wcześniej podawania maila na naszym portalu aby zalogować się przez konto społecznościowe. Do stylowania wykorzystałem formularze **Bootstrapa** .

Link do oficjalnej dokumentacji https://django-allauth.readthedocs.io/en/latest/installation.html

Pakiet **django-allauth** posiada gotowe formularze oraz widoki umożliwiająca szybkie dodawanie i tworzenie odpowiednich aplikacji. Do panelu admina dodaje on opcje umożliwiające zarządzanie aplikacjami społecznościowymi.

Po konfiguracji z oficjalnej dokumentacji django-allauth należy przystąpić do skonfigurowania aplikacji społecznościowych w panelu administratora oraz najpierw utworzyć połączenie do naszej aplikacji w panelu developera dostawcy. Ja wybrałem **Discord** i **Google** :

## Tworzenie aplikacji społecznościowej dla **Discorda**
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab3/zrzuty/9.PNG)
Tutaj znajdują się informacje takie jak klucz publiczny i prywatny oraz podajemy nazwę dla aplikacji i ważną rzeczą jest dodanie **Development callback URL** ,bez którego użytkownik nie zostałby przekierowany na naszą stronę. Można te informacje znaleźć pod tym odnośnikiem:https://django-allauth.readthedocs.io/en/latest/providers.html#discord

![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab3/zrzuty/10.PNG)
W zakładce **OAuth2** należy podać adres naszej domeny. Jest tutaj również istotna informacja o **ID klienta**.

![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab3/zrzuty/1.PNG)
Po utworzeniu aplikacji na stronie dostawcy należy utworzyć nową aplikację społecznościową w **panelu administratora**. Należy skopiować wszystkie istotne informacje ze strony dostawcy po czym podać domenę naszej aplikacji. 

## Tworzenie aplikacji społecznościowej dla **Google**
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab3/zrzuty/11.PNG)
Należy stworzyć aplikację ze strony : https://developers.google.com/ i wybrać **Google API Console**

![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab3/zrzuty/13.PNG)
Po utworzeniu aplikacji należy wejść w dane logowania i wybrać **OAuth client** 

![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab3/zrzuty/14.PNG)
Tak samo jak w przypadku **discorda** należy podać nazwę naszej domeny oraz **Development callback URL** i z tego miejsca należy skopiować **ID** i **klucz prywatny**

![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab3/zrzuty/2.PNG)
Po utworzeniu aplikacji na stronie **Google** pozostaje jedynie dodanie aplikacji w panelu administratora.

## Po dokonaniu wszystkich niezbędnych konfiguracji tak prezentuje się strona logowania:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab3/zrzuty/4.PNG)

Po wyborze logowania za pomocą **Google** przeniesie nas na stronę **Google** gdzie poprosi nas o zalogwanie się:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab3/zrzuty/5.PNG)

Po zalogowaniu się do konta **Google** przeniesie nas do strony głównej naszej aplikacji oraz doda do bazy danych inoformacje o użytkowniku(username pobierany jest z imienia przypisanego do konta Google):
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab3/zrzuty/6.PNG)

Po wyborze logowania za pomocą **Discorda** przeniesie nas na stronę **Discorda** gdzie również zostaniemy poproszeni o zalogwanie się(username pobierany z username'a Discorda):
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab3/zrzuty/7.PNG)

Po zalogowaniu się do **Discorda** powita nas strona główna naszej aplikacji:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab3/zrzuty/8.PNG)

Wszyscy użytkownicy są zapisani do bazy danych po zalogowaniu się przez konto społecznościowe a ich dane są pobierane do bazy.
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab3/zrzuty/15.PNG)

