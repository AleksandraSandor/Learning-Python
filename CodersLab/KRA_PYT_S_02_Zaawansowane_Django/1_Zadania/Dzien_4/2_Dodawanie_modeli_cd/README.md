# Dodawanie modeli do admina , cz. 2 &ndash; zadania

### Zadanie 1 &ndash; wykonywane razem z wykładowcą.

* Dodaj klasy admina do modelu `Book`. Niech edytowalne będą  wszystkie pola oprócz `added_date`.

---

### Zadanie 2.

* Dodaj klasy admina dla modelu `Author` i `Tag`.

### Zadanie 3.
* Zmodyfikuj klasy admina dla modeli biblioteki tak, by na liście obiektów pojawiały się:
    * dla modelu `Book`: tytuł, nazwisko autora, gatunek (słownie), właściciel i lista tagów,
    * dla modelu `Author` imię i nazwisko,
    * dla modelu `Tag` &ndash; tylko nazwa tagu.

* Tam, gdzie to konieczne, dodaj funkcje generujące odpowiednią etykietę.
* Ustaw standardowe sortowanie dla autorów: alfabetycznie wg nazwiska, książek &ndash; wg tytułu, tagów &ndash; wg nazwy.

### Zadanie 4. 
* Dodaj klasy admina dla modeli `Band`, `Album` i `Song`. 
* Zmodyfikuj klasy admina dla tych modeli tak, aby na liście pojawiały się:
    * dla modelu `Album`: tytuł albumu, nazwa zespołu i ranking (w postaci gwiazdek, czyli np. `****`, `***`) i rok wydania,
    * dla modelu `Band`: nazwa zespołu, rok założenia, i etykieta, czy nadal jest aktywny.
    * dla modelu `Song`: tytuł, album, czas trwania.

* Tam, gdzie to konieczne, dodaj funkcje generujące odpowiednią etykietę.
