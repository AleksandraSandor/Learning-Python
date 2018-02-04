from django.template.response import TemplateResponse
from django.shortcuts import render
from django.views import View
from Django_app.forms import UserLoginForm
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def	ship(request):
	ship = {
		"type":	"YT-1300	Light	Freighter",
		"name":	"Millenium	Falcon",
		"owner": "Han	Solo",
		"test": 4,
		"mac": {"k1": "v4",
		        "k2": "v5",
		        "k3": "v6"}
	}
	return render(request,	"ship.html", ship)
	
class Login(View):
	def get(self, request):
		form = UserLoginForm()#request.GET)
		return render(request, 'login.html', {'formm': form})
	def post(self, request):
		form = UserLoginForm(request.POST)
		if form.is_valid():
			pasword = form.cleaned_data['passw']
			usr = form.cleaned_data['usern']#form.cleaned_data['usern']
			if pasword == "a":
				# return HttpResponse("ok")
				return render(request, 'thx.html', {"form_w_html": usr})
		return HttpResponse("ok poza na koncu post")
			

# class MyFormView(View):
# 	def	get(self, request):
# 		form = NameForm()
# 		return render(request, 'login.html', {'form': form})
# 	def	post(self, request):
# 		form = NameForm(request.POST)
# 		if form.is_valid():
# 			login =	form.cleaned_data['login']
# 			# procesowanie	danych
# 			return	HttpResponseRedirect('/thanks/')
			
			
			
			
			
			
			# todo-------------------- str