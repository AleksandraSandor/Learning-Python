from django import forms
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth.models import User
# from .models import Notice


choices = (("1", "a"), ("2", "b"), ("3", "c"), ("4", "d"), ("5", "e"))

class UserLoginForm(forms.Form):
	usern = forms.CharField(label='Nazwa użytkownika',disabled = True, help_text = "za jakie grzeczy ?!", max_length=100, required = True) #, widget = forms.Textarea)
	passw = forms.CharField(label='Hasło', max_length=100, widget = forms.PasswordInput)
	opcje = forms.ChoiceField(label = "Pole wyboru", initial = "2", choices= choices, widget = forms.RadioSelect)#forms.Select)
	#  widget = forms.Select) forms.RadioSelect  forms.SelectMultiple, forms.MultipleChoiceField
		# widget=forms.PasswordInput())
	
		# //todo drugi dzien strona 39