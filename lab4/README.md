# Lab 4 – Tworzenie, edycja i usuwanie wpisów w Django

## Źródło

- [Strona źródłowa zadania](https://zacniewski.gitlab.io/teaching/2020-internet-apps/lab04/)

## Cel

W tym laboratorium dodasz funkcjonalności umożliwiające:

- dodawanie nowych wpisów,
- edytowanie istniejących,
- usuwanie wpisów.

## Krok po kroku

1. **Widoki (`views.py`)**:
   - `PostCreateView` – tworzenie wpisu (dziedziczy po `CreateView`)
   - `PostUpdateView` – edycja wpisu (`UpdateView`)
   - `PostDeleteView` – usuwanie wpisu (`DeleteView`)

2. **Szablony**:
   - `post_form.html` – wspólny dla tworzenia i edycji:
     ```django
     <form method="post">
       {% csrf_token %}
       {{ form.as_p }}
       <button type="submit">Save</button>
     </form>
     ```
   - `post_confirm_delete.html` – potwierdzenie usunięcia:
     ```django
     <form method="post">
       {% csrf_token %}
       <p>Are you sure you want to delete "{{ object }}"?</p>
       <button type="submit">Yes, delete</button>
     </form>
     ```

3. **Routing (`urls.py`)**:
   ```python
   path('post/new/', PostCreateView.as_view(), name='post_new'),
   path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
   path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
---

## Zadanie zostało wykonane od zera. Utworzone zostały 2 aplikacje: **Post** jako **api v1** oraz **testApp** jako **api v2** oraz zainstalowany został **Swagger** . DRF jest dużym udogodnieniem dla programisty, skraca potrzebny czas do tworzenia aplikacji oraz wymaga mniej kodu.

## Aplikacja Post(api v1):

### Po zalogowaniu jako użytkownik tak przedstawia się strona api/v1(metoda PostList z views):
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab4/zrzuty/3.PNG)

### Po wybraniu postu konkretnego jako autor zostanie wywołana metoda **PostDetail** i tak przedstawia się jej widok:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab4/zrzuty/1.PNG)
Jak widać u góry jest tam opcja **delete** .

### Po wybraniu postu jako osoba, nie będąca autorem tak przedstawia się widok:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab4/zrzuty/2.PNG)
Jak widać nie ma tam opcji Delete. Jest tak ponieważ w **permissions** została zdefiniowana metoda, która sprawdza czy dana osoba jest autorem posta

### Po wejściu na stronę nie bedąc zalogwany zostanie wyświetlony poniższy widok:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab4/zrzuty/4.PNG)

### Swagger przedstawia się następująco:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab4/zrzuty/5.PNG)
Jak widać są tam widoczne obie aplikacje.

### Tak przedstawia się widok dla metody get w intefejsie graficznym **Swaggera**
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab4/zrzuty/6.PNG)

### Dodany również został **Redoc** czyli dokumentacja naszego API DRF:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab4/zrzuty/7.PNG)

### Redoc przykład opcji **read**
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab4/zrzuty/8.PNG)

## Aplikacja testApp(api v2)
Dodane tutaj dodatkowo zostały:
- opcja wyszukiwania
- filtrowanie wyszykiwania
- oraz lekko zmodyfikowany serializer

### Tak przedstawia się api v2 gdy nie jesteśmy zalogowani
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab4/zrzuty/9.PNG)

### Tak przedstawia się api v2 gdy jesteśmy zalogowani
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab4/zrzuty/10.PNG)
Jak widać jest opcja filter, po której pokazuje się pasek wyszukiwania. Został on dodany z dokumentacji Django Rest Framework 
https://www.django-rest-framework.org/api-guide/filtering/ . We views'ach należało dodać **filter_backends = [filters.SearchFilter, filters.OrderingFilter]**,
**search_fields = ['title']** i **ordering_fields = ['title']** a w plikach **settings** **'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend',],** .
Dodatkowo należało pobrać pakiet **django filters**. Filtrowanie i wyszukiwanie odbywa się po parametrze **title**

### Tak przedstawia się wyszukiwanie po naciśnięciu guzika **filtry**
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab4/zrzuty/11.PNG)

### Po znalezieniu danego tytułu tak wygląda widok:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab4/zrzuty/12.PNG)
