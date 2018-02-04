from django.shortcuts import render
from django.views import View
from KRA_PYT_S_02_Warsztaty_3_app.models import Contact

class ContactListView(View):
    def get(self, request):
            contacts = Contact.objects.all()
            context = {"contacts":contacts,
                       "author" : "Wojtek",
                       "year" : "2017"}

            return render(request, "contact/contact_list.html", context)
