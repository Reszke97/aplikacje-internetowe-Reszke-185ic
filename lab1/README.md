# Lab 1 – Blog uruchomiony na PaaS

## Zadanie

- Utwórz repozytorium o nazwie `aplikacje-internetowe-nazwisko-185ic`, gdzie zamiast `nazwisko` wpisujesz swoje nazwisko lub numer indeksu.
- W tym repozytorium umieszczaj kolejne zadania w osobnych folderach z własnymi plikami `README.md`.

## Źródło

- [Strona źródłowa zadania](https://zacniewski.gitlab.io/teaching/2020-internet-apps/lab01/)

## Wymagane elementy:

Poniższe zagadnienia muszą zostać zrealizowane:

- instalacja pakietów i tworzenie projektu,
- korzystanie z serwera deweloperskiego,
- modele, migracje i ORM,
- ustawienia projektu,
- tworzenie superusera i panelu admina,
- tworzenie aplikacji w Django,
- QuerySets i menadżery obiektów,
- praca z plikami `views.py`, `urls.py` i szablonami,
- praca z formularzami (dodawanie posta, edycja istniejącego posta),

## Publikacja

- Blog należy uruchomić na platformie typu PaaS (np. [Heroku](https://www.heroku.com/), [PythonAnywhere](https://www.pythonanywhere.com/)).
- Dodatkowe punkty za przygotowanie widoku do [usuwania postów](https://zacniewski.gitlab.io/teaching/2020-internet-apps/lab01/#usuwanie).
- W przypadku Heroku konieczna będzie instalacja [Heroku-CLI](https://devcenter.heroku.com/articles/heroku-cli).

---


# Aplikacja została utworzona na serwerze Heroku.
#Link do strony na serwerze heroku:https://mareszkeblog.herokuapp.com/

## Strona główna bloga
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/zrzuty/1.PNG)

Stworzony został szablon główny **base.html**, z którego będzie korzystać każda podstrona. Do **urls** zostały dodane wszystkie z podstron. Na stronie po kliknięciu na guzik **+** jeśli jesteśmy zalogwani jako administrator zostaniem przeniesieni do dodania nowego posta. Jeśli klikniemy na którychś z tytułów to przenisie nas do edyci wybranego posta(również trzeba być zalogowany jako admin).

## podstrona dodaj nowy post:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/zrzuty/2.PNG)

## Gdy naciśniemy guzik zapisz zostaniemy przeniesieni do podstrony z nowo utworzonym postem:
Pojawia się opcja, w której możemy zedytować albo usunąć posta. Do stworzenia usuwania i edycji zostały stworzone osobne widoki oraz podczepione scieżki do nich w **urls**.
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/zrzuty/3.PNG)

## dodany post:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/zrzuty/6.PNG)

## Po wyborze opcji edytuj pojawia się nam następujące okno:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/zrzuty/4.PNG)
Po kliknięciu **zapisz** znowu zostanie nam wyświetlone okno z zedytowanym wcześniej postem

## Gdy wybierzemy opcje **usuń** to pojawi nam się następujące okno:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/zrzuty/5.PNG)
Po kliknięciu guzika usuń zostanie usunięty wybrany post

## Po usunięciu zostajemy przekierowani na stronę główną:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/zrzuty/7.PNG)
jak widać post został usunięty

## panel admistratora:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/zrzuty/8.PNG)
po wejściu na admina wyświetla nam się ten panel

## Widok konkretnego postu w panelu administratora:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/zrzuty/9.PNG)
