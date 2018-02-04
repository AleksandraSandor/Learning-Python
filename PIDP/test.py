# from Sets import Set
from collections import Counter


animals = ["pies", "kot", "chomik"]
for animal in animals:
    if animal == "pies":
        print("{} jest przyjacielem człowieka".format(animal))
    elif animal == "kot":
        print("{} jest franca".format(animal))
    elif animal == "chomik":
        print("{} jest szybki".format(animal))

print("wszystkie sa domowe")

lista = []
for i in range(1, 1000001):
    lista.append(i)

print(lista[0])
print(lista[-1])

print(min(lista))
print(max(lista))
print(sum(lista))

lista = []
for i in range(0, 21, 2):
    if i != 0:
        lista.append(i)

print(lista)


lista = []
for i in range(3, 31):
    i = i ** 3
    lista.append(i)

print(lista)
lista = [val ** 3 for val in range(1, 11)]
print(lista)
# for i in list:
#     print(i)

print("pierwsze 3 elementy listy to:\n")
print(lista[-3:])

animals_1 = animals[:]
animals.append("kanarek")
animals_1.append("owczarek")
print("{} i drugie {}".format(animals, animals_1))

proste_potrawy = ("żórek", "kilbasa", "kaszanka", "jajecznica", "nalesnik")
print(proste_potrawy)
for i in proste_potrawy:
    print(i)

print(proste_potrawy[0])
print("-------------------------")


proste_potrawy_lista = []
for i in proste_potrawy:
    proste_potrawy_lista.append(i)

print(proste_potrawy_lista)
proste_potrawy_lista.pop(1)
proste_potrawy_lista.pop(1)
print(proste_potrawy_lista)
proste_potrawy_lista.insert(1, "maslanka")
proste_potrawy_lista.insert(1, "kapusta")
print(proste_potrawy_lista)
proste_potrawy = tuple(proste_potrawy_lista)
print(proste_potrawy)

print(type(proste_potrawy))
print(type(proste_potrawy_lista))
print("------------")
tup = (1, 2, 3, 4)
lis = list(tup)
print(lis)

car = 'subaru'
print("czy car == 'subaru'? przewiduję wartość True.")
print(car == 'subaru')

print("czy car == 'audi'? przewiduję wartość False.")
print(car == 'audi')
a = 1
b = 5
# print(a.lower() < b)
# print(len(a) > len(b))
print(b in tup)

print("-----------------------")

# alien_color = ("zielony", "czerwony", "niebieski")
# alien_wybor = input("Jaki kolor:")
# punkty = 0
#
# while alien_wybor != "":
#     if alien_wybor == "zielony":
#         print("zarobiłeś 5 punktów")
#         punkty += 5
#     elif alien_wybor in alien_color:
#         print("zarobiłeś 2 punktów")
#         punkty += 2
#     alien_wybor = input("Jaki kolor:")
# print("Zdobyłeś: {} punktów".format(punkty))

print("-----------------------")
# age = 1
# while age != " ":
#     age = int(input("Ile masz lat:"))
#     if age < 2:
#         print("Niemowle")
#     elif (age >= 2) and (age < 4):
#         print("dziecko")
#     elif (age >= 4) and (age < 13):
#         print("starsze dziecko")
#     elif(age >= 13) and (age < 20):
#         print("nastolatek")
#     elif (age >= 20) and (age < 65):
#         print("dorosły")
#     elif (age >= 65):
#         print("Dziadek, babunia")

# fruits = ["jablko", "banan", "pomarancz"]
#
# fruit = input("Owoc:")
# if fruit in fruits:
#     print("Naprawdę lubisz {}".format(fruit))

class A():
    b = 10

x = 0
print(isinstance(x,A))
x = A()
print(isinstance(x,A))
print(i)
print("------------")
# users = ["admin", "bq666", "ula", "ala", "ola"]
# # users = []
# user = "test"
# while user != "":
#     user = input("Podaj nowy login:")
#     if user in users:
#         continue
#     else:
#         users.append(user)
#         break
#
#
# if users != []:
#     for user in users:
#         if user == "admin":
#             print("Witaj adminie, chcesz raport ?")
#         else:
#             print("Witaj {}".format(user))
# else:
#     print("musimy znaleść urzytkowników")
#
print("---------------")

lista = [x for x in range(1,11)]
for liczba in lista:
    if liczba not in [1,2,3]:
        print(str(liczba) + "th")
    else:
        if liczba == 1:
            print(str(liczba) + "st")
        elif liczba == 2:
            print(str(liczba) + "nd")
        elif liczba == 3:
            print(str(liczba) + "rd")
            
print("----------------------")
person = {"first_name":"Stefan",
          "last_name":"Stefanowski",
          "age":"39",
          "city":"Pizdnowo",}
print(person)

persons = {"woj":666,
           "waj":999,
           "lis":777,
           "as":27,
           "las": 111,}

# print(persons["woj"])

for person in persons:
    print("{} {}".format(person,persons[person]))
    
print("----------------")
glosariusz = {"PEP": "formatowanie",
              "Cpyton": "cos z C",
              "rekurencja": "zagnieżdzanie",
              "inkrementacja": "dodawanie 1",
              "konkantenacja": "dodawanie stringow",}

for definicja in glosariusz:
    print("Słowo: {} \n\tDefinicja: {}\n".format(definicja.title(),glosariusz[definicja]))
    
for key, value in glosariusz.items():
    print(key, value)
    
print("------------")

for name in sorted(glosariusz.values()):
    print(name)

glosariusz["test"] = "testowaty"
for name in sorted(glosariusz.values()):
    print(name)
print("-----------")
rzeki_kraje = {"egitp": "nil",
               "Srocz": "Wisła",
               "ble ble": "sciek",}

for rzeka in rzeki_kraje:
    print("{} płynie przez {}".format(rzeki_kraje[rzeka], rzeka))
print("---------")
for rzeka in rzeki_kraje.values():
    print(rzeka)

for panstwo in rzeki_kraje.keys():
    print(panstwo)
    
osoby = {"stef" : "1", "staf": "2", "stof": "3", "stor": "4", "star": "5"}
kursowe = {"stef": "6", "zez": "7", "zoz": "8", "zyz": "9", "zaz": "10",}
osoby.update(kursowe)
# nowy = dict(Counter(osoby) + Counter(kursowe))
print(osoby)

pies = {"rasa": "pis",
        "wilkosc": "sredni",
        "udomowienie": "tak",
        "agresja": "5",}

kot = {"rasa": "kot",
        "wilkosc": "maly",
        "udomowienie": "srednio",
        "agresja": "7",}

def show(dict):
    for k, v in sorted(dict.items()):#(dict.keys(), dict.values()):
        print(k , v)
        
show(pies)
print("----------")
show(kot)
print("__________________")
favorite_places = {"stef": ("arg", "las"),
                   "zuz": "srol",
                   "muz": "struz"}


for key in favorite_places:
    if type(favorite_places[key]) == tuple:
        for i in favorite_places[key]:
            print("Dla {} ulubione miejsce a to {}".format(key, i))
    else:
        print("Dla {} ulubione miejsce to {}".format(key, favorite_places[key]))
        

print("----------------------")
cites = {"war": {"country": "pol",
                 "pop": 666,
                 "fact": "stol",},
         "wro": {"country": "pol",
                 "pop": 66,
                 "fact": "piutifule",},
         "kra": {"country": "pol",
                 "pop": 99,
                 "fact": "vistula",},
         }

for cit in cites:
    print("__________________")
    print("Cechy dla miasta {}:".format(cit))
    for k in cites[cit]:
        print("{}: jest {}".format(k, cites[cit][k]))
        
print("---------------------")
# auto = input("Podaj markę jaka Cie interesuje: ")
# if auto == "auto":
# 	print("Słusznie")
# else:
# 	print("Bardziew")
# stolik = int(input("Jakiej wielkości chcesz stolik? :"))
# if stolik >= 8:
# 	print("Chcesz {} osobowy stolik, musisz poczekac".format(stolik))
# else:
# 	print('Prosze za mną')
# liczba = int(input("podaj liczbę"))
# if liczba % 10 == 0:
# 	print("Podana liczba jest wielokrotnoscią 10")
# else:
# 	print("nie podoba mi sie")
# test = True
# toppings = []
# while test:
# 	toppin = input("Podaj dodatek: ")
# 	if toppin != "koniec":
# 		toppings.append(toppin)
# 		print("Dodano {}".format(toppin))
# 	elif toppin == "koniec":
# 		test = False
# 	else:
# 		print("cos pokręciłeś")
# print("Wszystkie dodatki:")
# for toppin in toppings:
# 	print(toppin)


# while True:
# 	wiek = int(input("Podaj wiek: "))
# 	if wiek <= 3:
# 		print("Friko")
# 	elif (wiek > 3) and (wiek <= 12):
# 		print("10 slociszy")
# 	elif wiek > 12 and wiek < 200:
# 		print("dawaj 15 zet")
# 	elif wiek == 200:
# 		print("żegnam")
# 		break

# i = 0
# while True:
# 	print("Nieskończoność {}".format(i))
# 	i += 1
#
# print("-------------------")
# sandwich_orders = ["pyszna", "pastrami", "sraka", "pastrami", "taka sobie", "boska", "pastrami",]
# finisches_sandwiches = []
# print(sandwich_orders)
# print(finisches_sandwiches)
# print("nie ma pstrami")
#
# while sandwich_orders:
# 	if sandwich_orders[0] != "pastrami":
# 		print("Przygotowano: {}".format(sandwich_orders[0]))
# 		finisches_sandwiches.append(sandwich_orders[0])
# 		sandwich_orders.pop(0)
# 	else:
# 		sandwich_orders.pop(0)
#
# print(sandwich_orders)
# print(finisches_sandwiches)
#
# wakacje = " "
# wszystkie_wakacje = []
# while wakacje:
# 	wakacje = input("Gdzie byś pojechał jak byś mógł: ")
# 	wszystkie_wakacje.append(wakacje)
#
# print(wszystkie_wakacje)
print("----------------")
def messages():
	print("test wyswietlania")
	
messages()
print("--------------")
def book(book):
	print("Moja ulubiona książka to {}".format(book))

book("kniga")

def t_shirt(rozmiar = "XXL", tekst = "Uwielbiam pythona"):
	print("Zamówiłeś t-shirt:")
	print("Rozmiar {}".format(rozmiar))
	print("Tekst {}".format(tekst))
	
t_shirt("s", "dupa jas salata")
t_shirt(tekst="jas salata", rozmiar="SS")
t_shirt()
t_shirt("duży")

print("----------------")
def miasto(wielkosc = "duze", kraj = "sratoland"):
	print("Wielkość miasta to {} a jego polozenie to kraj {}".format(wielkosc, kraj))
	
miasto()
miasto("male", "pizdowo")
miasto("duzasne")
print("-----------")
def city_country(city, country):
	print(city , ",", country)
city_country("wawa", "pol")

# print("------------")
# dictionary = {}
# def make_album():
# 	while True:
# 		name = input("podaj name:")
# 		title = input("podaj title:")
# 		dictionary.update({name: title})
# 		if name == "0":
# 			break
# 	return dictionary
#
# albums = {}
# albums.update(make_album())
# print(albums)

print("---------")
magic = ["jeden", "coperfield", "hokus poku"]
def show_magic(magics):
	i = 0
	for magic_1 in magics:
		magics[i] = ("Doskonąły {}".format(magic_1))
		i += 1
	return magics
doskonaly_magisc = show_magic(magic[:])
show_magic(magic[:])
print(magic)
print(doskonaly_magisc)

print("------------")
def sandwich(*toppings):
	order = []
	for topping in toppings:
		order.append(topping)
	return order


a = sandwich("salata", "kapisuta", "pipusta")
b = sandwich("tylko raz")
print(a , "\n", b)

print("-----------")
def build_profile(first, last, **user_info):
	profile = {}
	profile["first name"] = first
	profile["last name"] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

my_profil = build_profile("wojtek", "gaudnik", location = "kraków", pasja = "programowanie")
print(my_profil)

print("-------------")
# import test_importu #<--- test_importu.car()
# from test_importu import car  #<---car()
# from test_importu import car as caaar  #<c--- aaar()
# import test_importu as mn #<---mn.car()
# from test_importu import *

# car_1 = car("audi", "tt", predkosc = " 300 km/h", kolor = "black")
# print(car_1)

def car(marka, model, **inne):
	car = {}
	car["marka"] = marka
	car["model"] = model
	for key, value in inne.items():
		car[key] = value
	return car

print("--------------")
class Restaurant(object):
	def __init__(self, name, type_r, number_reserved = 0):
		self.name = name
		self.type_r = type_r
		self.time = "9:00-23:00"
		self. number_reserved = number_reserved
	def opis(self):
		print("Nazwa restauracji to {} oraz jej typ to {}".format(self.name, self.type_r))
	def open(self):
		print("Godziny otwarcia {}".format(self.time))
		print("Rezerwacja na {}".format(str(self.number_reserved)))
	def set_res(self, number):
		self.number_reserved = number
	def set_res_up(self, number):
		self.number_reserved += number
		
res1 = Restaurant("pierwsza", "moja")
print(res1.name, res1.type_r)
res1.opis()
res1.open()
res2 = Restaurant("druga", "chinska")
res3 = Restaurant("trzecia", "wloska")
print(res2.name, res2.type_r)
print(res3.name, res3.type_r)
res2.opis()
res3.opis()

print("--------------")
class User(object):
	def __init__(self, name, last, age, high = 199, login = 0):
		self.name = name
		self.last = last
		self.age = age
		self.high = high
		self.login = login
	def describe(self):
		print("Witaj {} {}, twuj wiek to {}, a wzrost {}".format(self.name, self.last, str(self.age),
		                                                         str(self.high)))
	def greet(self):
		print("Specjalne powitanie dla {}{}{} zalogowanego {} razy".format(self.name, " ", self.last,
		                                                                   str(self.login)))
	def login_attempts(self,number):
		self.login += number
		if number == 666:
			self.login = 0
		
user1 = User("Stef", "Stachan", 34)
user1.describe()
user1. greet()
print("----------------")

res1 = Restaurant("italty", "italy", 133)
res1.open()
res1.number_reserved = 99
res1.open()
res1.set_res(666)
res1.open()
res1.set_res_up(-666)
res1.open()
print("-----------")
user1 = User("woj", "gau", 36, 166, 0)
user1.greet()
user1.login_attempts(2)
user1.greet()
user1.login_attempts(8)
user1.greet()
user1.login_attempts(666)
user1.greet()

print("---------------")
class IceCreamStand(Restaurant):
	def __init__(self, name, type_r, number_reserved=0, flavors = "vanilla"):
		super().__init__(name, type_r, number_reserved=0)
		self.flavors = flavors
	def smaki(self):
		print("Smaki:")
		for smak in self.flavors:
			print(smak)
		
lodziarka = IceCreamStand("Grycan", "home", 0, ("Czekoladowe", "Trusk", "winne"))
lodziarka.open()
lodziarka.opis()
lodziarka.smaki()

print("------------")
class Privilages():
	def __init__(self, privilages = ("moze usunąć usera", "moze zbanować usera",
	                                 "moze dodać usera")):
		self.privilages = privilages
	def show_privilges(self):
		print("Admin może:")
		for pri in self.privilages:
			print(pri)
	def add_priv(self, privil):
		self.privilages += privil

class Admin(User):
	def __init__(self, name, last, age, high=199, login=0):
		super().__init__(name, last, age, high, login)
		self.privilages = Privilages()
	# def show_privilges(self):
	# 	print("Urzytkownik {} to Admin i może:".format(self.name))
	# 	for pri in self.privilages:
	# 		print(pri)
			
admin_user = Admin("bog", "bozy", 66)
admin_user1 = Admin("boggg", "bozyyyy", 66666)
admin_user1.privilages.add_priv(("moze zawiesic",))

admin_user.privilages.show_privilges()
admin_user1.privilages.show_privilges()

admin_user2 = Admin("test", "testy", 999)
admin_user2.privilages.show_privilges()

print("----------------") #/todo TAK POWINNY WYGLĄDAĆ KLASY Z DZIEDZICZENIEM !!!
# class Car():
# 	"""Tutaj powinien być krutki docstring"""
# 	def __init__(self, make, model, year):
# 		"""Kolejny docstring"""
# 		self.make = make
# 		self.model = model
# 		self.year= year
# 		self.odometer_reading = 0
#
# 	def get_descriptive_name(self):
# 		"""Naastepny doc string"""
# 		long_name = str(self.year) + " " + self.make + " " + self.model
# 		return(long_name)
#
# 	def read_odometer(self):
# 		"""Doc string"""
# 		print("Ten samochód ma przejechane " + str(self.odometer_reading) + " km")
#
# 	def update_odometer(self, mileage):
# 		"""Doc string"""
# 		if mileage >= self.odometer_reading:
# 			self.odometer_reading = mileage
# 		else:
# 			print("Nie cofniesz licznika")
#
# 	def increment_odometer(self, kilometres):
# 		"""Doc string"""
# 		if kilometres >= 0:
# 			self.odometer_reading += kilometres
# 		else:
# 			print("Tak też nie cofniesz licznika")
#
# class Battery():
# 	"""Ta klasa będzie w klasie ElectricCar"""/todo
# 	def __init__(self, battery_size = 70):
# 		self.battery_size = battery_size
#
# 	def describe_battery(self):
# 		"""DocString"""
# 		print("Ten samochód ma baterie o pojemnosci " + str(self.battery_size) + "kWh")
# 	def get_range(self):
# 		"""DocString"""
# 		if self.battery_size == 70:
# 			range = 240
# 		elif self.battery_size == 85:
# 			range = 270
# 		message = "Zasięg tego samochodu to " + str(range)
# 		message += " po pełnym naładowaniu akumulatorów"
# 		print(message)
# 	def upgrade_battery(self):
# 		if self.battery_size != 85:
# 			self.battery_size = 85
#
# class ElectricCar(Car):
# 	"""DocString DZIEDZICZENIE"""
# 	def __init__(self, make, model, year):
# 		super().__init__(make, model, year)
# 		self.battery = Battery()
		
	
from test_importu import ElectricCar
my_car = ElectricCar("Audi", "TT", 2000)
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.battery.describe_battery()
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()

print("-------------")
from collections import OrderedDict
dict_order = OrderedDict()
# dict_order = {"1": 1}
dict_order["2"] = 2
dict_order["3"] = 3
dict_order["4"] = 4
dict_order["5"] = 5
dict_order["6"] = 6
dict_order["7"] = 7
dict_order["8"] = 8
print(dict_order)
for key, val in dict_order.items():
	print(key, str(val))
print("---")
for key, val in dict_order.items():
	print(key, str(val))
print("---")
for key, val in dict_order.items():
	print(key, str(val))

print("---")
from random import randint

class Die():
	def __init__(self, sides = 6, razy = 1):
		self.sides = sides
		self.razy = razy
	def roll_die(self):
		roll = []
		for i in range(0, self.razy):
			roll.append(randint(1, self.sides))
		return roll
	
kostka = Die(20,10)
print(kostka.roll_die())

print("-----------------")
with open("text.txt", "w") as file_object: #/todo tryby odczytu/zapisu r w a r+
	for i in range(100):
		file_object.write(str(i) + "  Uwielbiam programować \n")

with open("text.txt") as file_object:
	contents = file_object.readlines()
	for i in contents:
		print(str(contents + list("\n")))
	
	
print("--------------")
# with open("pi_million_digits.txt") as file_object:
# 	lines = file_object.readlines()
#
#
# pi_string = ''
# for line in lines:
# 	pi_string += line.strip()
#
# print(pi_string[:1052])
# print(len(pi_string))
#
# birthday = "280694"
#
# if birthday in pi_string:
# 	print("jest")
# else:
# 	print("nie ma")

print("---------")
with open("learning.txt") as file_object:
	print(file_object.read())
print("-")
with open("learning.txt") as file_object:
	test = True
	while test == True:
		line = file_object.readline()
		line = line.replace('pythonie', 'C')
		if line != "":
			print(line.strip())
		else:
			test = False
print("-")
with open("learning.txt") as file_object:
	line = file_object.readlines()
	print(line)



	