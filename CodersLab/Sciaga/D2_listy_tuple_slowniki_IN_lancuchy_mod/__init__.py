# ===============================================================================
#                 LISTY
# ===============================================================================
bbt = ["Leonard", "Sheldon", "Penny", "Howard", "Raj", "Bernadette", "Amy"]
print(bbt)
print("    0           1         2         3       4         5          6")
print(bbt[0])
print(bbt[4])
print(bbt[-1])
print(bbt[-7])
print(bbt[2:4])  # prawo stronnie otwate
print(bbt[4:])
print(bbt[2:])
print(bbt[:2])
print(bbt[-3:])
print(bbt[:-3])
print(bbt[2:-2])
print(bbt[0:7:2])
print(bbt[4:2:-1])

mix_types = ["ala", 23, True, "23", "test", 1, 2, 3, 4, 5, 6]

print(type(mix_types))
print(mix_types)
print(len(mix_types))
for i in mix_types:
    print(i, type(i))

mix_types.pop(0)  # <---------------------------------------tablica.pop ----------------usuwanie pozycji z listy
print(mix_types)
mix_types.append(
    "ala")  # <---------------------------------------tablica.append--------------dodawanie pozycji do listy
print(mix_types)
for i in mix_types[:-1:2]:
    print(i)

my_list = []
for i in range(0, 10):
    my_list.append(i * 4)
print(my_list)

my_list = [4 * i for i in range(0, 10)]
print(my_list)

my_list = [9 * i for i in range(0, 10) if i % 4 == 0]
print(my_list)
a1 = ["a", "b", "c", "d", "e", "f"]
a2 = ["honda", "sronda", "fiat", "audi"]
a = a1 + a2
a.append("e")  # <--- dodaje na końcu
a.insert(3, "e")  # <--- dodaje w konkretny index
del a[3]  # <--- usuwa i przesuwa do konkrentego indexu
a.pop(3)  # <--- usuwa i przesuwa do konkrentego indexu
a.remove("b")  # <--- usuwa pierwsze wystapienie
a.sort()  # <--- sortuje na stale, tylko listy itp.
b = sorted(a)  # <--- sortuje ale nie zmienia kolejności na stałe
b.reverse()
b = b.reverse()
print(b)
a = list(range(1, 16))
print(a)
a = list(range(0, 101, 5))
print(a)
print(max(a))
print(min(a))
print(sum(a))
print(sum(a) / len(a))
a = [2 ** i for i in range(1, 11)]
# ===============================================================================
#        KROTKI(TUPLE)
# ===============================================================================
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, "test", "test"]
print(lista)
tupla = (10, 11, 12, 13, 14, 15, 16, 17, 18, 18, "test", "test")
print(tupla)

tupla_z_listy = tuple(lista)
print("tupla z listy:", tupla_z_listy)

lista_z_tupli = list(tupla)
print("lista z tupli:", lista_z_tupli)
# ===============================================================================
#         SŁOWNIKI(DICTIONARY)
# ===============================================================================
star_wars = {
    "episode": 4,
    "title": "A New Hope",
    "characters": ["Luke", "Leia", "Han Solo", "Obi-Wan", "Chewbacca", "Vader", "C3P0", "R2D2"]}
test = {"a": [1, 2, 3], "b": [4, 5, 6]}

print(test)

print(star_wars["episode"])
print(star_wars["characters"])

star_wars["year"] = 1976  # <--------------Dodawnie klucza i wartosci do słownika
print(star_wars)
star_wars["year"] = 1977  # <--------------Modyfikowanie wartosci klucza
print(star_wars)
del (star_wars["year"])  # <--------------Usówanie klucza
print(star_wars)

print("--------------------------")
for key in star_wars:
    print(key)

print("--------------------------")
for key in star_wars:
    print(key, star_wars[key], end="  koniec\n", sep=" : ")  # .join("test")

print("---{} ____2{}".format(" abra", " kadabra"))
print("------".join("ABRA"))
# ===============================================================================
#             SŁOWO KLUCZOWE  ----IN------
# ===============================================================================
droids = ["C3P0", "R2D2", "BB-8"]
for dro in droids:
    print(dro)

starship = {
    "type": "X-wing",
    "allegiance": "Resistance",
    "owner": ["Poe Dameron", "Pa Pou"]
}
for fea in starship:
    print(fea, starship[fea], sep=": ")

if "BB-8" in droids:
    print("BB-8 jest w droids")
else:
    print("BB-8 nie ma w droids")

if "Pa Pou" in starship["owner"]:
    print("Pa Pou jest")
else:
    print("Pa Pou nie ma")
# ===============================================================================
#             ŁAŃCUCHY TEKSTOWE
# ===============================================================================
lancuch_tekstowy = "123456789 abcdefghijklmnoprstuwxyz !@#$%^&*()"
dlugi_lancuch_txt = """ to jest 
    bardzo
    długi
    łancuch
    tekstowy
"""
print(lancuch_tekstowy)
print(dlugi_lancuch_txt)
print(lancuch_tekstowy[0:10:2])
print(lancuch_tekstowy[::-1])
print("Bilbo " + "Bagins")

hobbits = ("Frodo", "Sam", "Merry", "Pippin")
desc = ("Hobbits in LOTR: %s, %s, %s" + " and %s.") % hobbits
print(desc)

hobbit = {
    "name": "Bilbo Baggins",
    "occupation": "burglar"
}
description = "%(name)s is a %(occupation)s." % hobbit  # <-------- PRZESTARZAŁE Z PYTHONA 2
print(description)

description = "{} is a {}".format("Gandalf The Grey", "wizard")  # <----- FORMATOWANIE OK !!!
print(description)

description = "{} is a {}".format(hobbit["name"], "wizard")  # <----- FORMATOWANIE OK !!!
print(description)
# ===============================================================================
#         MODUŁY
# ===============================================================================
import datetime  # funkcje na czas i date
import math  # funkcje matematyczne
import os  # integracja z sytemem
import urllib  # biblioteki do łączenia z serveerami
import curses  # zaawansowana obsługa terinala

import random  # liczby pseudolosowe

los = random.randint(10, 20)
print(los)

import calendar

day = calendar.weekday(1977, 5, 25)
print(calendar.day_name[day])

from calendar import weekday, day_name

day = weekday(1977, 5, 25)
print(day_name[day])

print(day)
print(calendar.day_name)
print(calendar.day_name[6])

# from D2_.hobbit_mod import *
#from D2_listy_tuple_slowniki_IN_lancuchy_mod.hobbit_mod import (hobbit, descfiption)

# print(hobbit)
# print(descfiption())

# ===============================================================================
#                             KONIEC
# ===============================================================================
