# Uprawnienia i widoki &ndash; zadania

### Zadanie 1 &ndash; wykonywane z wykładowcą.

Ogranicz dostęp do widoku `/add_user` tylko do superużytkowników.

---

### Zadanie 2.
Ogranicz dostęp do widoku `/album_list` tylko dla zalogowanych użytkowników.

### Zadanie 3. 
Zwróć uwagę, że dostęp do widoków dodawania / modyfikowania / usuwania albumów ograniczany jest tylko przez wyświetlanie / niewyświetlanie konkretnych linków w widoku `/album_list`. Gdy wejdziemy ręcznie na odpowiedni widok, możemy robić co chcemy z albumami.

Dodaj takie ograniczenia dostępu, żeby:
* tylko użytkownik z uprawnieniem "add_album" mógł dodać album,
* tylko użytkownik z uprawnieniem "change_album" mógł modyfikować album,
* tylko użytkownik z uprawnieniem "delete_album" mógł usunąć album.
