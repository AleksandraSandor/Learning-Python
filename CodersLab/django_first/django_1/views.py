# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseNotFound # HttpResponseNotFound("nie znależiono strony")
from random import randint
from django_1.models import Product
from django_1.models import Opinion
from django_1.models import Discount
from django_1.models import OrderData
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from datetime import timedelta
import tzlocal
from django.core.exceptions import ObjectDoesNotExist
import pytz

from django.shortcuts import render

# Create your views here.
def	losowa(request):
    los = randint(0,100)
    html = """
		<html>
		<body>
			<p>Wylosowano liczbę: %s</p>
		</body>
	</html>
	""" % los
    return	HttpResponse(html)

def	show_number_with_max(request, max_num):
    los = randint(0,100)
    max_num = int(max_num)
    random_max_num = randint(0, max_num)
    html = """
		<html>
		<body>
			<p>Wylosowano liczbę z max %s: %s</p>
		</body>
	</html>
	""" % (max_num, random_max_num)
    return	HttpResponse(html)

def show_number_with_min_max(request, min_num, max_num):
    max_num = int(max_num)
    min_num = int(min_num)
    random_max_num = randint(min_num, max_num)
    html = """
    		<html>
    		<body>
    			<p>Wylosowano liczbę z zakresu %s - %s wylosowana: %s</p>
    		</body>
    	</html>
    	""" % (min_num, max_num, random_max_num)
    return HttpResponse(html)

def show_name(request, name):
    name += " Test"
    html = """
    		<html>
    		<body>
    			<p>Witaj %s !</p>
    		</body>
    	</html>
    	""" % (name)
    return HttpResponse(html)

def show_name(request, name):
    name += " Test"
    html = """
    		<html>
    		<body>
    			<p>Witaj %s !</p>
    		</body>
    	</html>
    	""" % (name)
    return HttpResponse(html)

def add_product(request):
    html = """
        		<html>
        		<body>
        			<p>Dodałem product</p>
        		</body>
        	</html>
        	"""
    p = Product()
    p.name = "dlugopis"
    p.description = "rozowy"
    p.price = 3.50
    p.available = True
    p.save()
    return HttpResponse(html)

def add_product_small(request):
    html = """
        		<html>
        		<body>
        			<p>Dodałem product_small 1</p>
        		</body>
        	</html>
        	"""
    t = Product.objects.create(name="anchovies", price=3.50)
    #p = Pizza.objects.create(size=2)
    return HttpResponse(html)

def get_product(request, id_prod):
    #prod = Product.objects.get(pk = id_prod)
    prod_name = Product.objects.get(name = id_prod)
    #t = Product.objects.create(name="anchovies", price=3.50)

    html = """
            		<html>
            		<body>
            			<p>Product z id %s to %s</p>
            			<p>Opis:</p>
            			<p>Id: %s </p>
            			<p>name: %s </p>
            			<p>description: %s </p>
            			<p>price: %s </p>
            		</body>
            	</html>
            	"""% (id_prod, prod_name.name, id_prod, prod_name.name, prod_name.description, prod_name.price) #prod.name, prod.description,
    #p = Pizza.objects.create(size=2)
    return HttpResponse(html)

def all_product(request):
    list = Product.objects.all()
    html = ""
    for row in list:
        html += "{} {} </br>".format(row.id, row.name)
    return HttpResponse(html)

def get_product_by_name(request, price):
    price = float(price)
    list = Product.objects.filter(price__lte = price)
    html = ""
    for row in list:
        html += "{} {} {} </br>".format(row.id, row.name, row.price)
    return HttpResponse(html)

def get_product_by_name_and_id(request, price, name_my):
    #price = float(price)
    list = Product.objects.filter(price__lte = price).filter(name = name_my)
    html = ""
    for row in list:
        html += "{} {} {} </br>".format(row.id, row.name, row.price)
    return HttpResponse(html)

def get_by_price(request, price):
    html = ""
    list = Product.objects.filter(price__lt = price)
    html += "---------------------LT</br>"
    for row in list:
        html += "{} {} {} </br>".format(row.id, row.name, row.price)
    list = Product.objects.filter(price__lte = price)
    html += "---------------------LTE</br>"
    for row in list:
        html += "{} {} {} </br>".format(row.id, row.name, row.price)
    list = Product.objects.filter(price__gt = price)
    html += "---------------------GT</br>"
    for row in list:
        html += "{} {} {} </br>".format(row.id, row.name, row.price)
    list = Product.objects.filter(price__gte = price)
    html += "---------------------GTE</br>"
    for row in list:
        html += "{} {} {} </br>".format(row.id, row.name, row.price)
    return HttpResponse(html)

def filter_description(request, name_my):
    list = Product.objects.filter(name__contains = name_my)
    html = "---------------------</br>"
    for row in list:
        html += "{} {} {} </br>".format(row.id, row.name, row.price)
    html += "---------------------</br>"
    return HttpResponse(html)

def some_id(request, id_1, id_2):
    list = Product.objects.filter(id__in = [id_1, id_2])
    html = "---------------------</br>"
    for row in list:
        html += "{} {} {} </br>".format(row.id, row.name, row.price)
    html += "---------------------</br>"
    return HttpResponse(html)

def modify_product(request, id_1, new_price):
    list = Product.objects.get(id = id_1)
    #list.price = 3
    html = ""
    html += "------------Cena przed {} </br>".format(list.price)
    list.price = new_price
    list.save()
    list = Product.objects.get(id = id_1)
    html += "------------Cena po {}".format(list.price)
    return HttpResponse(html)

def add_opinions(request):
    # relation between product and opinion: one - many
    prod = Product.objects.get(id = 2)
    opinion = Opinion()
    opinion.description = "Bardzo smaczne"
    opinion.product = prod
    opinion.save()
    opinion2 = Opinion()
    opinion2.description = "Uwielbiam to"
    opinion2.product = prod
    opinion2.save()
    return HttpResponse("Dodano opinie")

def get_opinions(request):
    # relation between product and opinion: one - many
    prod = Product.objects.get(id = 2)
    opinions = Opinion.objects.filter(product = prod)
    html = "Opinie na temat produktu {} o id={}<br/>".format(prod.name, prod.id)
    for opinion in opinions:
        html += opinion.description + "<br/>"
    return HttpResponse(html)

def add_opinion(request, id_my, description):
    # relation between product and opinion: one - many
    id_my = int(id_my)
    prod = Product.objects.get(id = id_my)
    opinion = Opinion()
    opinion.description = description
    opinion.product = prod
    opinion.save()

    # prod = Product.objects.get(id = 2)
    # opinion = Opinion()
    # opinion.description = "Bardzo smaczne"
    # opinion.product = prod
    # opinion.save()
    # opinion2 = Opinion()
    # opinion2.description = "Uwielbiam to"
    # opinion2.product = prod
    # opinion2.save()
    return HttpResponse("Dodano opinie, hurrrraaaaa")

def add_discount(request):
    product = Product.objects.get(pk = 2)
    discount = Discount()
    discount.value_in_percent = 15.0
    discount.product = product  #<--- /todo CO TO
    discount.save()

    return HttpResponse("Dodano rabat!")

def get_discount(request):
    PRODUCT_ID = 2
    prod = Product.objects.get(pk = PRODUCT_ID)
    discount = Discount.objects.get(product = prod)
    html = "Rabat równa się: {}".format(discount.value_in_percent)
    return HttpResponse(html)

def add_order(request):
    PRODUCT_ID = 2
    order = OrderData()
    order.description = "Super wazne zamowienie!!!"
    order.save()
    prod1 = Product.objects.get(pk=PRODUCT_ID)
    prod2 = Product.objects.get(pk=PRODUCT_ID + 1)
    # order.products.add(prod1)
    # order.products.add(prod2)
    prods = [prod1, prod2]
    order.products.set(prods)
    order.save()
    return HttpResponse("Zlozono nowe zamowienie")

def get_order(request):
    ORDER_ID = 2
    order = OrderData.objects.get(pk=ORDER_ID)
    html = "Zamówienie o ID={} i opisie: {} zawiera produkty: (liczba={}):<br/>".format(order.id,
                                                                                         order.description,
                                                                                         len(order.products.all()))
    for prod in order.products.all():
        html += "{}, price: {}<br/>".format(prod.name, prod.price)
    return HttpResponse(html)

def det_order_by_id(request, my_id):
    order = OrderData.objects.get(pk = my_id)
    html = "Zamówienie o ID={} i opisie: {} zawiera produkty: (liczba={}):<br/>".format(order.id,
                                                                                        order.description,
                                                                                        len(order.products.all()))
    for prod in order.products.all():
        html += "{}, price: {}<br/>".format(prod.name, prod.price)
    return HttpResponse(html)

# def delete_from_order(request, order_id, prod): #/todo Nie kurwa dziala !!!!!
#     order = OrderData.objects.get(pk = order_id)
#     prod = Product.objects.get(name = prod)
#     order.products.remove(prod)
#     order.save()
#     html = "Usuniete"  #/todo sprawdź ę
#     return HttpResponse(html)

def get_order_by_product_id(request):
    PRODUCT_ID = 1
    prod = Product.objects.get(pk=PRODUCT_ID)
    orders_where_this_product_is_present = prod.orderdata_set.all()
    html = "Produkt o id = {} występuje na zamówieniach: <br/>".format(prod.id)
    for order in orders_where_this_product_is_present:
        html += "id: {}, description: {} <br/>".format(order.id, order.description)

    return (HttpResponse)
#/todo########################################################
#/todo GET GET GET GET GET GET GET GET GET GET GET GET GET GET
#/todo########################################################

def calculate_power_2(request):
    value = request.GET.get("num")
    age = request.GET.get("age")
    value = int(value)
    if value is None:
        return HttpResponse("Brak parametru")
    power_2 = 2 ** value
    return HttpResponse("{}:</br>2^{} = {}".format(age, value, power_2))

def zad_1(request):
    start= int(request.GET.get("start"))
    end = int(request.GET.get("end"))
    html = ""
    for i in range(start, end):
        html += "{} </br>".format(i)
    return HttpResponse(html)

def tabliczka(request):
    width = int(request.GET.get("width"))
    height = int(request.GET.get("height"))
    html = "width = {}, height = {}</br>".format(width,height)
    html += "__"
    for i in range(1, width):
        html += str(i)
        html += " "
        for ii in range(1, height):
            html += str(i*ii)
        html += "</br>"
    return HttpResponse(html)

@csrf_exempt
def login_form(request):
    if request.method == "GET":
        html = """
            <HTML>
                <BODY>
                    <FORM METHOD='POST'>                        
                        Login: <INPUT type='text' name='login' />
                        Password: <INPUT type='password' name='password' />
                        <INPUT type='submit' />                         
                    </FORM>
                </BODY>
            <HTML>
        """
        return HttpResponse(html)
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")
        if (login is not None) and (password is not None):
            return HttpResponse("Przesłano dane, l: {}, p: {}".format(login, password))

@csrf_exempt
def hello_1(request):
    if request.method == "GET":
        html = """
            <HTML>
                <BODY>
                    <FORM METHOD='POST'>                        
                        Imie: <INPUT type='text' name='imie' />
                        Nazwisko: <INPUT type='text' name='nazwisko' />
                        <INPUT type='submit' />                         
                    </FORM>
                </BODY>
            <HTML>
        """
        return HttpResponse(html)
    if request.method == "POST":
        imie = request.POST.get("imie")
        nazwisko = request.POST.get("nazwisko")
        if (imie is not None) and (nazwisko is not None):
            return HttpResponse("Przesłano dane, imie: {}, nazwisko: {}".format(imie, nazwisko))



@csrf_exempt
def temp(request):
    if request.method == "GET":
        html = """
            <HTML>
                <BODY>
                    <form action="#" method="POST">
                        <label>
                            Temperatura:
                            <input type="number" min="0.00" step="0.01" name="degrees">
                        </label>
                        <input type="submit" name="convertionType" value="celcToFahr">
                        <input type="submit" name="convertionType" value="FahrToCelc">
                    </form>
                </BODY>
            <HTML>
        """
        return HttpResponse(html)
    if request.method == "POST":
        degrees = int(request.POST.get("degrees"))
        val=request.POST.get("convertionType")
        if val == "celcToFahr":
            temp = 32 + (9/5) * degrees
        else:
            temp = (5/9) * (degrees - 32)
        return HttpResponse(temp)


@csrf_exempt
def login_form_session(request):
    if request.method == "GET":
        html = """
            <HTML>
                <BODY>
                    <FORM METHOD='POST'>                        
                        Login: <INPUT type='text' name='login' />
                        Password: <INPUT type='password' name='password' />
                        <INPUT type='submit' />                         
                    </FORM>
                </BODY>
            <HTML>
        """
        if request.session.get("logged_in") == True:
            request.session["ile"] += 1
            return HttpResponse("Witaj {}! Jesteś zalogowany od godziny : {} Odświerzyłęś strone {}".format(request.session.get("name"),
                                                                                     request.session.get("started"),request.session.get("ile")))
        return HttpResponse(html)
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")
        STORED_PASSWORD_FOR_RAFAL = 'rafal'
        if login == 'rafal' and password == STORED_PASSWORD_FOR_RAFAL:
            request.session["logged_in"] = True
            request.session["name"] = login
            #now = datetime.now(pytz.timezone('Europe/Warsaw'))
            now = datetime.now(tzlocal.get_localzone())   #timedelta
            request.session["started"] = now.now().strftime("%Y-%m-%d %H:%M:%S")
            return HttpResponse('Zalogowano')
        return HttpResponse("Błędny login lub hasło")
        if (login is not None) and (password is not None):
            return HttpResponse("Przesłano dane, l: {}, p: {}".format(login, password))

def login_out(request):
    request.session['logged_in'] = False
    return HttpResponse('Wylogowano')

#@csrf_exempt
def setSession(request):
    if request.method == "GET":
        request.session['counter'] = 0
    html = "Counter = {}".format(request.session.get('counter'))
    return (HttpResponse(html))

def showSession(request):
    if request.method == "GET":
        html = "Counter = {}".format(request.session.get('counter'))
        request.session['counter'] += 1
    else:
        html += "Miałeś wejść GET !!!"
    return HttpResponse(html)


def deleteSession(request):
    if request.method == "GET":
        request.session['counter'] = None
        # request.session.clear()
        # request.session["loggerUser"] = ""
    return HttpResponse('Wylogowano')


@csrf_exempt
def login(request):
    # request.session.clear()
    if request.method == "GET":
        if request.session.get("loggedUser") == "":
            html = """
                <HTML>
                    <BODY>
                        <form action="#" method="POST">
                            <label>
                                Imię:
                                <input type="text" name="name">
                            </label>
                            <input type="submit" name="convertionType">
                            {% csrf_token %}
                        </form>
                    </BODY>
                <HTML>
            """
            return HttpResponse(html)
        if request.session.get("loggedUser") != "":
            return HttpResponse("GET'em i loggerUser jest cos jest")
    if request.method == "POST":
        name = request.POST.get("name")
        request.session["loggerUser"] = name
        return HttpResponse("POST'em i loggerUser jest {}".format(request.session.get("loggerUser")))

@csrf_exempt
def addToSession(request):
    if request.method == "GET":
        html = """
            <HTML>
                <BODY>
                    <form action="#" method="POST">
                        <label>
                            Klucz:
                            <input type="text" name="key">
                        </label>
                        <label>
                            Wartość:
                            <input type="text" name="value">
                        </label>
                        <input type="submit" name="convertionType">
                        {% csrf_token %}
                    </form>
                </BODY>
            <HTML>"""
        return HttpResponse(html)

    if request.method == "POST":
        key = request.POST.get("key")
        value = request.POST.get("value")
        request.session[key] = value
        request.session['all'] = ''
        for key in request.session.keys():
            request.session['all'] += 'Klucz: %s, Wartość: %s ,</br>' % (key,request.session.keys())
        return HttpResponse("Pobrano dane")


def showAllSession(request):
    return HttpResponse(request.session.get('all'))


def session_clear(request):
    request.session.clear()
    return HttpResponse("Sesja wyczyszczona")

def session_print(request):
    html = ""
    for key in request.session.keys():
        html += " {} : {} </br>".format(key, request.session.get(key))
    return HttpResponse(html)

@csrf_exempt
def session_add_form(request):
    html_form = """    
            <HTML>
                <BODY>
                    <form action="#" method="POST">
                        <label>
                            Klucz:<input type="text" name="key">                        
                            Wartość:<input type="text" name="value">
                        </label>
                        <input type="submit" name="convertionType">
                        {% csrf_token %}
                    </form>
                </BODY>
            <HTML>"""
    if request.method == "GET":
        return HttpResponse(html_form)

    if request.method == "POST":
        key_from_form = request.POST.get("key")
        value_from_form = request.POST.get("value")

    request.session[key_from_form] = value_from_form
    return HttpResponse("Dodano do sesji")

def mojastrona(request, nazwa):
    html = "jest OK!"
    html += nazwa
    return HttpResponse(html)

#--------------------------- COOKIES
def cookie_set(request):
    response = HttpResponse("Dodano ciasteczko")
    exp = datetime.now() + timedelta(hours = 2)
    response.set_cookie("ciasteczko1", "wartosc ciasteczka", expires = exp)
    return response

def cookie_get(request):
    value = request.COOKIES.get("ciasteczko1")
    return HttpResponse(value)

def cookie_clear(request):
    response = HttpResponse("Ciasteczka wyczyszczone")
    for cookie_name in request.COOKIES.keys():
        response.delete_cookie(cookie_name)
    return response

def cookie_print(request):
    html = "Cookies:</br>"
    for cookie_name in request.COOKIES.keys():
        html += "key: {} value: {} </br>".format(cookie_name, request.COOKIES.get(cookie_name))
    return HttpResponse(html)

@csrf_exempt
def cookie_add_form(request):
    html_form = """    
            <HTML>
                <BODY>
                    <form action="#" method="POST">
                        <label>
                            Klucz:<input type="text" name="key">                        
                            Wartość:<input type="text" name="value">
                        </label>
                        <input type="submit" name="convertionType">
                        {% csrf_token %}
                    </form>
                </BODY>
            <HTML>"""
    if request.method == "GET":
        return HttpResponse(html_form)

    if request.method == "POST":
        key_from_form = request.POST.get("key")
        value_from_form = request.POST.get("value")
        response = HttpResponse("Dodano ciasteczko")
        exp = datetime.now() + timedelta(hours=4)
        response.set_cookie(key_from_form, value_from_form, expires=exp)
        return response




def set_as_favourite(request, my_id):
    try:
        my_id = int(my_id)
        prod = Product.objects.get(pk=my_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("404  nie znależiono indexu")
    except Exception:
        return HttpResponseNotFound("Nie znależiono strony")
    exp = datetime.now() + timedelta(hours=4)
    response = HttpResponse("Dodano ciasteczko o id {} z zespołem {}".format(my_id, prod.name))
    response.set_cookie(str(my_id), "{}".format(prod.name), expires=exp)
    return response






