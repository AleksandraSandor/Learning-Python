from django.shortcuts import render
from django.http import HttpResponse
from D9_Django_app.models import Product, Topping, Pizza
from random import randint
# def show_number(request, number):
#       return HttpResponse(html)
#       Product.objects.create(name=i, description=opis[randint(0, 4)], price=randint(0, 1000))
#       prod = Product.objects.get(pk=3)
#       prods = Product.objects.all()
#       prod_filter = Product.objects.filter(name="trzy")
#       prod_filter = Product.objects.filter(name = "dwa",description = "rewelacja")
#       prod_filter = Product.objects.filter(price__lt = 500.0)  __lt __lte __gt __gte
#       prod_filter = Product.objects.filter(name__in=['jeden', 'dwa'])
#       prod_filter = Product.objects.filter(name__contains = "jeden")
#       prod = Product.objects.get(pk=20)   <---
#       prod.price = 666.66                 <---
#       prod.save()                         <---
#       prod.delete() <--- bez save
#       tops = [t1, t2]         #/todo set !!!
#       p.toppings.set(tops)    #/todo set !!!
#       p.toppings.remove(t2)   #/todo usuwanie 1 dodatku do pizzy
#       p.toppings.clear()      #todo usuwanie wszystkich dodatków
#       p = Pizza.objects.get(pk=1)
#       toppings = p.toppings.all()
#       for topping in toppings:  # /todo wyciąganie wszystkich dodatków na pizzy
#       html += topping.name + "</bre>"  # /todo wyciąganie wszystkich dodatków na pizzy






# Create your views here.
def show_number(request, number):
    html = """
    <html>
		<body>
			<p>The	answer	is	%s!</p>
		</body>
	</html>
	""" % number
    return HttpResponse(html)

def add(request):
    html = "Udało się"
    products = ["jeden", "dwa", "trzy", "cztery", "piec"]
    opis = ["fajn", "lepszy", "gorszy", "taki sobie", "rewelacja"]
# /todo -----------dodawanie wierszy:
    for i in products:
        Product.objects.create(name = i, description = opis[randint(0,4)], price = randint(0,1000))
    return HttpResponse(html)

def show(request):
    prod = Product.objects.get(pk=3)
    html = prod.name
    html += "----------------------"
    prods = Product.objects.all()
    for prod in prods:
        html += prod.name
        html += " "
        html += prod.description
        html += "</br>"
# /todo -----------filtr po 2 różnych kolumnach w tabeli:
    html += "----------------------Product.objects.filter(name = 'dwa',description = 'rewelacja')</br>"
    prod_filter = Product.objects.filter(name = "dwa",description = "rewelacja")
    for prod_f in prod_filter:
        html += str(prod_f.name) + " " + str(prod_f.price) + "</br>"
# /todo -----------filtr z zakresów:
    prod_filter = Product.objects.filter(price__lt = 500.0).filter(price__gt = 200)
    html += "----------------------Product.objects.filter(price__lt = 500.0).filter(price__gt = 200)</br>"
    for prod_f in prod_filter:
        html += prod_f.name + " " + str(prod_f.price) + "</br>"
# /todo -----------filtr po 1 wartosci ale wszystkie znajduje:
    prod_filter = Product.objects.filter(name__contains = "jeden")
    html += "----------------------Product.objects.filter(name__contains= 'Jeden')</br>"
    for prod_f in prod_filter:
        html += prod_f.name + " " + str(prod_f.price) + "</br>"
# /todo -----------filtr po 2 wartosciach:
    prod_filter = Product.objects.filter(name__in=['jeden', 'dwa'])
    html += "----------------------prod_filter = Product.objects.filter(name__in=['jeden', 'dwa'])</br>"
    for prod_f in prod_filter:
        html += prod_f.name + " " + str(prod_f.price) + "</br>"
# /todo -----------zmiana danych:
#     prod = Product.objects.get(pk = 20)
#     prod.price = 666.66
#     prod.save()
#     html += "----------------------po zmianie ceny na 666.66</br>"
#     prods = Product.objects.all()
#     for prod in prods:
#         html += str(prod.id) + " " + prod.name + " " + prod.description + " " + str(prod.price) + "</br>"
# /todo -----------usówanie danych cały wiersz :
#     prod = Product.objects.get(pk = 22)
#     prod.delete()
#     prods = Product.objects.all()
#     html += "----------------------usówanie </br>"
#     for prod in prods:
#         html += str(prod.id) + " " + prod.name + " " + prod.description + " " + str(prod.price) + "</br>"
# /todo -----------relacja wiele do wielu dodawanie i tworzenie
#     html += "----------------------relacja wiele do wielu dodawanie i tworzenie </br>"
#     t1 = Topping.objects.create(name = "anochovies", price = 3.5)
#     t2 = Topping.objects.create(name="onion", price = 2.00)
#     p = Pizza.objects.create(size = 1)
#     p.toppings.add(t1)  #/todo p<---object Pizza  toppings<---pole w relacji Pizza  add <--- metoda  t1<--- dodatek
#     p.toppings.add(t2)
#     html += "Dodano dodatki i powiazano z pizza </br>"
#     pizzas = Pizza.objects.all()
#     html += "----------------------relacja wiele do wielu metodą set() </br>"
#     for pizza in pizzas:
#         html += " id:" + str(pizza.id) + "  size:" + str(pizza.size) + "</br>"
#     p = Pizza.objects.create(size=2)
#     t1 = Topping.objects.get(pk=1)
#     t2   = Topping.objects.get(pk=2)
#     tops = [t1, t2]
#     p.toppings.set(tops) #/todo set !!!


    p = Pizza.objects.get(pk=3)
    p.toppings.remove(t2)                   # todo usuwanie 1 dodatku do pizzy
    p.toppings.clear()                      # todo usuwanie wszystkich dodatków
    html += "udało się </br>"
    html += "</br> ----------------------wyciąganie wszystkich dodatków na pizzy </br>"
    p = Pizza.objects.get(pk=1)
    toppings = p.toppings.all()
    for topping in toppings:                # todo wyciąganie wszystkich dodatków na pizzy
        html += topping.name + "</br>"      # todo wyciąganie wszystkich dodatków na pizzy
    html += "</br>----------------------wyciąganie wszystkich pizz z dodatkiem </br>"
    t = Topping.objects.get(pk=2)
    pizzas = t.pizza_set.all()              # todo pizza_set. automatycznie w trakcie budowania relacji
    for test in pizzas:                     # todo wyciąganie wszystkich pizz z dodatkiem
        html += str(test.id) + "</br>"      # todo wyciąganie wszystkich pizz z dodatkiem


    return HttpResponse(html)



    # -------------------------KONIC !!!!