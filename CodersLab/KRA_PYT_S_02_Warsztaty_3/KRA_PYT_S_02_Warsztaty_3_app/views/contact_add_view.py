from django.shortcuts import render
from django.views import View
from KRA_PYT_S_02_Warsztaty_3_app.models import Contact
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
class ContactAddView(View):
    def get(self, request):
        context = {"author" : "Wojtek",
                   "year" : "2017"}
        return render(request, "contact/contact_add.html", context)
    def post(self, request):
        # Validate input from form
        contact = Contact()
        contact.name = request.POST.name
        contact.surname = request.POST.surname
        contact.description = request.POST.description
        contact.save()
        return HttpResponseRedirect("/contact/list")