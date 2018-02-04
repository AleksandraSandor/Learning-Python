# Dodawanie modeli do admina &ndash; zadania

### Zadanie 1 &ndash; wykonywane z wykładowcą.
* Sprawdź, czy admin jest poprawnie skonfigurowany,
* Dodaj do admina model `Student`.

### Zadanie 2.
* Dodaj do admina pozostałe modele dotyczące muzyki: `SchoolSubject` i `StudentGrades`,
* Wyedytuj dane. Czy widzisz jakiś problem?

### Zadanie 3.
* Dodaj do admina resztę modeli.

### Zadanie 4.
* Nadpisz czytelnie metodę `__str__()` modeli, które używasz.

### Zadanie 5.
Wyobraź sobie aplikację, która pozwala użytkownikom katalogować swoje książki. Zdefiniuj modele:
* `Author`:
    * imię,
    * nazwisko.

* `Book`:
    * tytuł,
    * gatunek: wybierany z listy:
        * kryminał,
        * sci-fi/fantasy/horror,
        * literatura faktu,
        * poradnik,
        * obyczajowa,
    * autor: klucz obcy do modelu `Author`,
    * właściciel: klucz obcy do modeelu `User`, który jest zdefiniowany w Django,
    * czy wypożyczona?
    * data dodania: data automatycznie dodawana podczas zapisu.

* `Tag` to etykiety (słowa kluczowe), których możemy dodać wiele do każdej książki:
    * nazwa.

* Zdefiniuj odpowiednią relację: każda książka może mieć wiele tagów, każdy tag może być przypisany do wielu książek.
* Zdefiniuj odpowiednie modele w adminie.
