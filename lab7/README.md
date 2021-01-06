# Praca z Redisem + Django + Celery na systemie Windows 10 jest bardzo trudna ponieważ Celery od wersji 4.0 nie jest wspierane na Windowsie o czym dokładnie pokaże później.
# Przechodząc dalej to wykonałem projekt ze strony https://stackabuse.com/asynchronous-tasks-in-django-with-redis-and-celery/ oraz zadania od Pana Mazurka ze strony https://mmazurek.dev/tag/redis-i-python/?order=asc.

## W pierwszej kolejności wykonałem ciąg zadań o Redisie:

### Uruchomienie redisa:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/1a.PNG)

### Sprawdzenie poprawności Redisa. Tutaj pobrałem rozszerzenie do visual studio z konsolą redisa i komendą ping sprawdziłem poprawność działania

### Tworzenie pary klucz i wartość
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/1.PNG)

### Tworzenie pary klucz i wartość gdzie zwracany jest string
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/2.PNG)

### Dołączenie do istnijącej wartości nowego stringa
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/3.PNG)

### Usunięcie istniejącego klucza i wartości
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/4.PNG)

### Dodawanie/Odejmowanie wartości od typu liczbowego
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/5.PNG)

### Tworzenie listy
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/6.PNG)

### Tworzenie listy ora jej wyświetlenie w podanym przedziale
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/7.PNG)

### Metoda blokująca wykonywanie programu(brpop)
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/8.PNG)

### Za pomocą RPUSH dodałem do listy element i jak widać po dodaniu elementu program zaczał działać wyszedł ze stanu zablokowania
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/9.PNG)

### Dodanie i pobranie elementów do/ze zbiorów
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/11.PNG)

### Praca na posortowanych zbiorach
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/12.PNG)

### Posortowane zbiory o tej samej wadze
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/13.PNG)

### Praca z Hashami - wykorzystanie metody **HGETALL**(wyświetla pare klucz wartość)
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/14.PNG)

### Praca z Hashami - wykorzystanie metody **HKEYS**(wyświetla tylko nazwy kluczy)
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/15.PNG)

### Praca z Hashami - wykorzystanie metody:
    - HEXISTS(sprawdza czy dany klucz istnieje)
    - HVALS(wyświetla tylko wartość bez klucza w słowniku)
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/16.PNG)

### Metoda Pop w liście
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/17.PNG)

### Pubsub
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/18.PNG)

### Wykorzystanie strumieni
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/19.PNG)

### Pubsub metoda **xadd**
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/20.PNG)


### Strumienie Point - dodaje nowe dane do strumienia i są one wyświetlane
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/22.PNG)

### Stumienie z pokazanym poprawnym odbieraniu elementów
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/23.PNG)

### Pipelining benchmark(Jak widać na poniższym zdjęciu jest to użycie Pipeliningu mocno przyspiesza wykonywanie programu)
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/24.PNG)

### Redis+Lua - wykonanie prostego skryptu zwracającego string
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/25.PNG)

### Redis+Lua - przekazywanie parametrów do skryptu
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/26.PNG)

### Redis+Lua - Wygenerowanie liczb wewnątrz Lua:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/27.PNG)

### Lua z JSON'em
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/28.PNG)

### Redis+Lua - Pobranie z Redisa danych i przetworzenie ich i zapisanie wyniku
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/29.PNG)

### Wynik z poprzedniego zadania w Redisie:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/30.PNG)

### Redis+Lua - Utworzenie uprawnień i nowej grupy użytkonwików
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/31.PNG)

### Uprawnienia w Redisie po wykonanym działaniu programu:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/32.PNG)

### Redis+Lua przykład jak w skrócony sposób wywołać wykonany wcześniej skrypt:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/33.PNG)

### Nasłuchiwanie na każdą zmianę klucza wynikającą z komend dedykowanych stringowi(jak widać najpierw ustawiamy do wartości klucza 15 potem za pomocą append dodajemy do niego 11):
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/34.PNG)

### Po wykonaniu LPUSH jak widać wartość zostaje nadpisana
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/35.PNG)

### Nasłuchiwanie na każdą zmianę klucza wynikającą z komend dedykowanych stringowi(widać tutaj dodatkowo nazwę klucza)
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/36.PNG)

# Rozpoczęcie Projektu ThumbNailer

## Przed rozpoczęciem pracy z celery należy zainstalować następujące pakiety:
- pip install Django Celery redis Pillow django-widget-tweaks

## Celery nie działa poprawnie na windowsie od wrsji 4.0 tutaj podaje link do oficajnej dokumentacji https://docs.celeryproject.org/en/stable/faq.html#does-celery-support-windows
## Tak więc aby celery poprawnie działało niezbędne było najpierw zainstalowanie pakietu **gevent** za pomocą polecenia:
```python
pip install gevent
```
## Przed zainstalowaniem pakietu potrzebne było również zainstalwanie visual c++ tools. https://github.com/benfred/implicit/issues/76 

## Po zainstalowaniu pakietu, celery odpalamy następującą komendą:
```python
celery -A mysite worker -l info -P gevent
```
## Do wykonania prostyh tasków działała również komenda:
```python
celery -A mysite worker -l info -P threads
``` 
## W przeciwnym razie task zostanie otrzymany lecz zawsze będzie w stanie **Pending**

## Utworzenie pierwszego Taska oraz uruchomienie celery
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/37.PNG)

## Sprawdzanie tasku czy działa:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/39.PNG)

# Wdrożenie projektu thumbnailer

## Do pliku settings należy dodać następujące linie kodu:
```python
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media'))
IMAGES_DIR = os.path.join(MEDIA_ROOT, 'images')

if not os.path.exists(MEDIA_ROOT) or not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

# celery
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Warsaw' 
```

## Oraz do installed apps dodać następujące linie kodu:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Redis.apps.RedisConfig',
    'widget_tweaks',#<-------------------to
    'django_celery_beat',#<---------------------to
]
```

## W części task niezbędne było również zmodyfikowanie kodu ponieważ kod ze strony nie działał na moim systemie w oczekiwany sposób tj. Nie zmieniał zdjęcia na rozmiar 128x128px ponieważ wyskakiwał mi błąd systemu :
```python
celery WARNING/MainProcess] [WinError 32] The process cannot access the file because it is being used by another process:
```
## Był to najprawdopodobniej jakiś błąd z uprawnieniami systemu windows 10

## Program w pliku tasks pobiera i kopiuje obrazek i oblicza wymiary na miniature, następnie zapisuje kopie oryginalnego obrazu i zapisuje miniature po czym pakuje je dodatkowo do pliku zip. Tak przedstawia się zmodyfikowany kod:
```python
import os
from zipfile import ZipFile


from celery import shared_task

from PIL import Image

from django.conf import settings

@shared_task
def make_thumbnails(file_path, thumbnails=[]):
    os.chdir(settings.IMAGES_DIR)
    path, file = os.path.split(file_path)
    file_name, ext = os.path.splitext(file)

    zip_file = f"{file_name}.zip"
    results = {'archive_path': f"{settings.MEDIA_URL}images/{zip_file}"}
    try:
        img = Image.open(file_path)
        zipper = ZipFile(zip_file, 'w')
        zipper.write(file)
        #os.remove(file_path)<-------------niezbędne było usunięcie tej lini kodu
        for w, h in thumbnails:
            img_copy = img.copy()
            img_copy.thumbnail((w, h))
            thumbnail_file = f'{file_name}_{w}x{h}.{ext}'
            img_copy.save(thumbnail_file)
            zipper.write(thumbnail_file)
            #os.remove(thumbnail_file)<-------------niezbędne było usunięcie tej lini kodu

        img.close()
        zipper.close()
    except IOError as e:
        print(e)

    return results
```
## Po tych modyfikacjach celery wykonywał obróbkę zdjęcia:

## Tak przedstawia się gotowa strona:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/40.PNG)

## Proces obróbki zdjęcia:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/41.PNG)

## Zdjęcie zostało pobrane
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/42.PNG)

## Zawartość wypakowanego archiwum
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/43.PNG)

## Tak przedstawia się stworzony wcześniej folder media/images po obróbce zdjęcia, jak widać są tam oba zdjęcia jedno po obróbce a drugie przed
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/44.PNG)

## Tak przedstawia się konsola po wykonaniu zadania obróbki zdjęcia(pol prawej stronie zapytania do serwera a po lewej konsola celery). Tutaj odpalam już celery komendą:
```python
celery -A mysite worker -l info -P gevent
```
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/45.PNG)

# Praca z Celery Beat

## Potrzebne było zainstalowanie następujących pakietów:

- pip install python-crontab

- pip install django-celery-beat

## Utworzenie tasków w pliku tasks:
```python
# Taski okresowe

# Task wykonywany o określonym czasie
@shared_task(name='test')
def send_notifiction():
     print('Hello there mortals')
     # Another trick

# Task wykonywany co 10 sekund
@shared_task(name='summary') 
def send_import_summary():
    print('Hello there every 10 sec')
```
## Teraz należy w pliku settings dodać następujący kod:
```python
# Time Tasks With Celery
from celery.schedules import crontab
CELERY_BEAT_SCHEDULE = {
'beat co 10 sekund': { #<---------- taki komunikat będzie otrzymaniu taska
       'task': 'summary',#<------- task name
       'schedule': 10.0#<---------- co ile sekund
    },
    # Wykonuj sie o godzinie 15:00
    'Witaj o 15:05': {  #<---------- taki komunikat będzie otrzymaniu taska
         'task': 'test', #<------- task name
         'schedule': crontab(hour=15, minute=5), #<określona godzina
    },
}
```

## Teraz komendą: 
```python
celery -A mysite beat -l INFO --scheduler 
django_celery_beat.schedulers:DatabaseScheduler
```
## Włączam celery beat, następnie komendą:
```python
celery -A mysite worker -l info -P gevent
```
## Uruchamiam celery

## Tak przedstawiają sie konsole po włączeniu celery beat:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/46.PNG)

## Dodatkowo po zainstalowaniu celery beat i dodaniu w kodzie tasków w panelu administratora pojawia się nam Okno Periodic Task gdzie możemy dodawać nowe taski. Dodałem nowy Task o nazwie **Marik1234**. Jak widać można tam wybrać gotowy task z kodu.
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/47.PNG)

## Tak przedstawia się task przeze mnie napisany, który dodałem przez panel administratora:
```python
@shared_task(name='AdminPanel')
def send_import_summary():
    print('Dodano mnie przez panel admina')
```

## Tak przedstawiają się konsole po dodaniu taska:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/48.PNG)

## Na zdjęciu poniżej widać wszystkie taski:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab7/zrzuty/49.PNG)

