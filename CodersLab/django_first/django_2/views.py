# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def	hello(request):
	html = """
	<html>
		<body>
			<p>Hello World</p>
		</body>
	</html>
	"""
	return	HttpResponse(html)