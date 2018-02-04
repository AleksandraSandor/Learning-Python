print("hello world")
a = "to jest tekst do testu"
print(a)
print(a.title())
print(a.upper())
print(a.lower())

mac = "to ta ta to"
mac_upper = mac.upper()
print(mac_upper)
print(mac)

a = "     sratatata     r  "
print(a)
print(a.rstrip())
print(a.lstrip())
print(a.strip())

a = ["a", "b", "c", "d"]
print(a)
a.append("e")  # <--- dodaje na końcu
print(a)
a.insert(3, "e")  # <--- dodaje w konkretny index
# print(a)
del a[3]  # <--- usuwa i przesuwa do konkrentego indexu
# print(a)
a.pop(3)  # <--- usuwa i przesuwa do konkrentego indexu
print(a)
a.remove("b")  # <--- usuwa pierwsze wystapienie
# print(a)
a = ["test", "ala", "ma", "kota", "chyba"]
# a = "co za kurwa mac"
print(a)
a.sort(key=None, reverse=False)  # <--- sortuje na stale, tylko listy itp.
print(a)
a = ["honda", "sronda", "fiat", "audi"]
b = sorted(a)  # <--- sortuje ale nie zmienia kolejności na stałe
print(b)
print(a)
b.reverse()
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
b = "testowanie"
print(b)
print(a, b)

imie = "stefania stefanowska"
print("witaj " + imie.title() + " co dzisiaj robimy!?!")

cytat = '   powiedział \tkiedyś że "gówno równo"\t\t'
autor = "Albert Einstein"

# cytat = cytat.strip()
print(autor + cytat + autor)
print(5 + 3)
print(11 - 3)
print(4 * 2)
print(32 / 4)
ulubiona = 666
print("Moja ulubina liczba to ", ulubiona)

imiona = ["stefan", "stafan", "stofan", "sreran"]
print(imiona[0])
# print(imiona[:])
for name in imiona:
    print("witaj " + name)
    print()
from random import randint
auta = ("Honda", "Audi", "rower")
a = randint(0,2)

auto = auta[a]

print("Pojeździł bym " + auto.title())

osoby = ["Stef", "Hanna", "Zuzanna"]


osoba_no = osoby[randint(0,2)]
print(osoba_no, "Nie przyjdzie")
osoby.remove(osoba_no)
osoby.append("Tadeusz")
osoby.insert(2,"Obenar")
osoby.insert(2,"Urwana")
print(osoby)
for osoba in osoby:
    print("Zapraszam ", osoba)

#del osoby[randint(0,len(osoby) - 1)]
#osoba_no = osoby.pop(randint(0,len(osoby) - 1))
print(osoba_no)
#osoba_no = osoby.pop(randint(0,len(osoby) - 1))
print(osoba_no)
print(osoby)
for osoba in osoby:
    print("Zapraszam ", osoba)

miejsca = ["Austalia", "Argentyna", "Alaska", "Gruzja", "Włochy"]
posortowane = sorted(miejsca)
print(posortowane)
print(miejsca)
posortowane = sorted(miejsca,reverse = True)
print(posortowane)
posortowane = sorted(miejsca,reverse = False)
print(posortowane)
posortowane.reverse()
print(posortowane)
posortowane.reverse()
print(posortowane)
posortowane.sort(reverse=True)
print(posortowane)
print(len(osoby))

baza = {"miasta":["Krakow", "wawa", "wroc"], "panstwa":["USA", "ARG", "Gruz"]}
print(baza)
for i in baza:
    print(i)
    for ii in baza[i]:
        print(ii)

test = baza["panstwa"]
print(test)
print(test[2])
