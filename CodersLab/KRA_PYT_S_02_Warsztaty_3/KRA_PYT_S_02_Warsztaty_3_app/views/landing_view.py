from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse

class LandingView(View):
    def get(self, request):
        # context = {"author" : "Wojtek",
        #            "year" : "2017"}
    	return render(request, "landing.html")#, context)

    def post(self, request):
    	return HttpResponse("Przyszedł request POST")



