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
