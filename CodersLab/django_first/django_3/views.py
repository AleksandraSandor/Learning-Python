# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from random import randint
from django_1.models import Product
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
    p.descryption = "rozowy"
    p.price = 3.50
    p.available = True
    p.save()
    return HttpResponse(html)

