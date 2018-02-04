from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, EmailValidator
from django.forms import Form, ModelForm

from .models import SCHOOL_CLASS, Topping


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError("{} nie jest parzyste!".format(value))


def validate_year(value):
    if value not in (2002, 2003, 2004):
        raise ValidationError("Rok urodzenia powinien być w zakresie 2002–2004!")    


class NameForm(Form):
    number = forms.IntegerField(label="wpisz liczbę",
                                widget=forms.Textarea,
                                validators=[validate_even, ])


class StudentSearchForm(Form):
    surname = forms.CharField(label="Wprowadź nazwisko")


class AddStudentForm(Form):
    first_name = forms.CharField(label="Imię ucznia")
    last_name = forms.CharField(label="Nazwisko ucznia")
    school_class = forms.ChoiceField(label="Klasa", choices=SCHOOL_CLASS, help_text="Wybierz klasę, do której chodzi uczeń")
    year = forms.IntegerField(label="Rok urodzenia",
                              validators=[validate_year, ])


additional_ingredients = (
        (0, "oliwki"),
        (1, "pomidory"),
        (2, "dodatkowy ser"),
        (3, "anchovies"),
        (4, "cebula"),
    )


class ComposePizzaForm(Form):
    ingredients = forms.MultipleChoiceField(label="dodatkowe składniki",
                                            choices=additional_ingredients,
                                            widget=forms.CheckboxSelectMultiple
                                            )


class PresenceListForm(Form):
    student = forms.IntegerField(widget=forms.HiddenInput)
    day = forms.DateField(widget=forms.HiddenInput)
    present = forms.NullBooleanField()


class UserForm(Form):
    first_name = forms.CharField(label="Imię")
    last_name = forms.CharField(label="Nazwisko")
    email = forms.CharField(label="email",
                            validators=[EmailValidator(), ])
    www = forms.CharField(label="Ulubiona strona WWW",
                          validators=[URLValidator(), ])


class ToppingForm(ModelForm):
    class Meta:
        model = Topping
        fields = "__all__"
        
        
        







from django import forms
from django.contrib.auth.models import User
from .models import Notice

class UserLoginForm(forms.Form):
	username = forms.CharField(label='Nazwa użytkownika', max_length=100)
	password = forms.CharField(label='Hasło', max_length=100,
		widget=forms.PasswordInput())


def validate_firstletter(value):
	'''
	Sprawdzamy, czy pole spełnia nasze wymaganie, tzn. czy zaczyna się od x
	'''
	if value.startswith('xxx'):
		raise ValidationError("{} nie zaczyna się od xxx!".format(value))

class UserCreateForm(forms.Form):
	username   = forms.CharField(label='Nazwa użytkownika', max_length=100)
	password1  = forms.CharField(label='Hasło', max_length=100,
		widget = forms.PasswordInput())
	password2  = forms.CharField(label='Hasło (ponownie)', max_length=100,
		widget = forms.PasswordInput())
	first_name = forms.CharField(label='Imię', max_length=100)
	last_name  = forms.CharField(label='Nazwisko', max_length=100, validators=[validate_firstletter,])
	email      = forms.CharField(label='Email', max_length=100,
		widget = forms.EmailInput())


	def clean(self):
		cleaned_data = self.cleaned_data
		password1 = cleaned_data.get("password1")
		password2 = cleaned_data.get("password2")

		if password1 != password2:
			self._errors["password1"] = self.error_class(['Podane hasła nie są jednakowe'])

		return cleaned_data

	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username = username).exists():
			raise forms.ValidationError('Login zajęty')
		return username # + 'XXXX'


class ChangePassUserForm(forms.Form):
	password1  = forms.CharField(label='Hasło', max_length=100,
		widget = forms.PasswordInput())
	password2  = forms.CharField(label='Hasło (ponownie)', max_length=100,
		widget = forms.PasswordInput())

	def clean(self):
		cleaned_data = self.cleaned_data
		password1 = cleaned_data.get("password1")
		password2 = cleaned_data.get("password2")

		if password1 != password2:
			self._errors["password1"] = self.error_class(['Podane hasła nie są jednakowe'])

		return cleaned_data


class NoticeCreateForm(forms.ModelForm):
	class Meta:
		model = Notice
		fields = ['description',]
