# Lab 2 – Rejestracja użytkowników

## Źródło
🔗 https://zacniewski.gitlab.io/teaching/2020-internet-apps/lab02/
---

# Aplikacja została utworzona na serwerze Heroku.
## Do edycji wyglądu formularza wykorzystałem bootstrapa. Aby to osiągnąć najpierw tworzyłem bazowy formularz Django a następnie kopiowałem elementy formularza Django do ostylowanych formularzy bootstrapa. Dodatkowo zastosowałem mechanizm wykrywania błędów metodą **if form.errors** i przechodząc w pętlach po wszystkich wystąpnieniach błędów a następnie jeśli takowe wystąpiły to wypisane zostały w formolarzu inforumjąc użytkownika co należy poprawić.
#Link do strony na serwerze heroku:https://mareszkeblog.herokuapp.com/

## Strona główna bloga
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/1.PNG)

Do szablonu base.html została dodana ikona kłódki po której naciśnięci pokaże nam się strona na której mamy opcje **zalogowania się**, **restu hasła** lub **rejestracji** konta

## Strona logowania:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/2.PNG)
Z tej podstrony jest możliwość przejścia do **zalogowania** **rejestracji** lub **restu hasła**

## Strona Rejestracji
Tutaj można utworzyć konto
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/3.PNG)

## Gdy źle podamy hasła lub nie bedą one spełniać warunków to po przesłaniu formularza otrzymamy komunikat o błędzie
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/7.PNG)

## Po udanym procesie rejestracji zostaniemy przeniesieni na stronę główną
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/5.PNG)

## Po ponownym przejściu na podstronę logowania i po zalogowaniu tak wygląda strona główna. Jak widać jest tam opcja **dodaj post/wyloguj/zmień hasło** oraz wiadomość witająca użytkownika.
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/11.PNG)

## Widok zmiany hasła
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/12.PNG)

## Po podaniu niepoprawnych danych i przesłaniu formularza dostaniemy informacje o błędzie
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/13.PNG)

## Udana zmiana hasła
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/14.PNG)

## Widok resetu hasła
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/15.PNG)

## Po przesłaniu formularza z resetem wyświetli się poniższy komunikat
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/16.PNG)

## Dodanie maila do istnięjącego w bazie danych użytkownika za pomocą konsoli
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/17.PNG)

## Panel administratora po dodaniu maila użytkownikowi w konsoli
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/18.PNG)

## Po wysłaniu formularza w konsoli serwera wyświetli się poniższy komunikat z linkiem do zmiany hasła
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/19.PNG)

## Po kliknięciu w link pokaże się strona z opcją zmiany hasła:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/20.PNG)

## Po poprawnej zmianie hasła wyświetli się wiadomość:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/22.PNG)

## Teraz możemy się zalogować na konto ze zmienionym hasłem:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab2/zrzuty/23.PNG)
