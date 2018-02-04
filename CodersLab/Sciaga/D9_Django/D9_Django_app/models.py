from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    available_from = models.DateField(null=True)

PIZZA_SIZES	=	((1,	"small"),(2,	"medium"),(3,	"big"),)
class Topping(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
class Pizza(models.Model):
	size = models.IntegerField(choices=PIZZA_SIZES)
	toppings = models.ManyToManyField(Topping)




# Create your models here.
# /todo-----------POLA:
# name    =   models.CharField(max_length=64)  <---Standardowe pole tekstowe typu VARCHAR
# content =	models.TextField() <--- Standardowe	pole tekstowe typu VARCHAR, ale	bez	ograniczenia długości tekstu.
# score	=	models.SmallIntegerField() <--- Przechowuje	wartości z zakresu	od -32768 do 32767.
# price	=	models.DecimalField(max_digits=5, decimal_places=2) <--- Decimal
# wants_spam	=	models.BooleanField() <---Pole	przechowujące True lub False. Nie może mieć wartości NULL.
#                 models.NullBooleanField()     <---Pole	przechowujące True lub False lub NULL
#                 models. DateField() <--- Mapowane do pola DATE
# available_from	=	models.DateTimeField() <--- Mapowane do pola DATETIME.
# visits	=	models.IntegerField() <---Standardowe pole liczbowe typu INTEGER
# /todo----------Parametry pul:
# models.<typ-pola>(attr_1=val_1,	...	,attr_n=val_n)
# score	=	models.IntegerField(default=0) <---Ustawia standardową	wartość danego pola
# name	=	models.CharField(max_length=64,null=True) <---null ustawione na True, to pole może przechowywać NULL
# LIGHTSABERS	=	((1,	"Red"),(2,	"Blue"),(3,	"Green"),(4,	"Purple"))#
# saber	=	models.IntegerField(choices=LIGHTSABERS)<---
# games_played	=	models.IntegerField(db_index=True) <---ustawione na	True,to	pole jest indeksem w bazie danych.
# my_id	=	models.CharField(max_length=6,	primary_key=True) <--- 	żeby klucz główny obiektu był nadany
# Do klucza głównego możemy	dostać się na dwa sposoby: Nazwa pola id, lub Właściwość pk bez względu na nazwę klucza
# /todo----------Relacje:
# class Cart(models.Model):             #/todo <--- wiele do jednego
# 	user = models.ForeignKey(User)      #/todo <--- wiele do jednego
#
# class Discount(models.Model):                                                             #/todo <--- 1 do 1
# 	user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)       #/todo <--- 1 do 1
#
# PIZZA_SIZES	=	((1,	"small"),(2,	"medium"),(3,	"big"),)#/todo <--- wiele do wielu
# class Topping(models.Model):                                      #/todo <--- wiele do wielu
#     name = models.CharField(max_length=32)                        #/todo <--- wiele do wielu
#     price = models.FloatField()                                   #/todo <--- wiele do wielu
# class Pizza(models.Model):                                        #/todo <--- wiele do wielu
# 	size = models.IntegerField(choices=PIZZA_SIZES)                 #/todo <--- wiele do wielu
# 	toppings = models.ManyToManyField(Topping)                      #/todo <--- wiele do wielu
#---------------------------------------------------------------------------------------------
# TOP_AMOUNT	=	(('h',	'half'),('n',	'normal'),('d',	'double'),('t',	'triple'))
# class	PizzaTops(models.Model):
# 				pizza	=	models.ForeignKey(Pizza)
# 				topping	=	models.ForeignKey(Topping)
# 				amount	=	models.CharField(max_length=1,	choices=TOP_AMOUNT,	default='n')
# class	Pizza(models.Model):
# 				size	=	models.IntegerField(choices=PIZZA_SIZES)
# 				toppings	=	models.ManyToManyField(Topping,	through=PizzaTopps)
# class Topping(models.Model):
#     name = models.CharField(max_length=32)
#     price = models.FloatField()
#       /todo To już w views !!!!
# pt = PizzaTopps.objects.create(pizza=p, topping=t1, amount='n')
# Zwróć	uwagę,że do pola relacji przekazujemy cały model,nie tylko jego id.
#---------------------------------------------------------------------------------------------