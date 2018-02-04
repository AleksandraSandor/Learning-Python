from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.edit import FormView, CreateView

from .models import (SCHOOL_CLASS, Student, SchoolSubject, StudentGrades,
                     PresenceList, Topping)

from .forms import (NameForm, StudentSearchForm, AddStudentForm,
                    ComposePizzaForm, PresenceListForm, UserForm, ToppingForm)

from django.contrib.auth.models import User



# models.py

# Create your views here.
class SchoolView(View):

    def get(self, request):
        classes = []
        for school_class in SCHOOL_CLASS:
            classes.append(school_class[1])
        return render(request, "school_view.html",
            {"classes": classes})


class SchoolClassView(View):

    def get(self, request, school_class):
        students = Student.objects.filter(school_class=school_class)
        return render(request, "class.html", {"students": students,
                                              "class_name": SCHOOL_CLASS[int(school_class) - 1][1]})

class MyObj:
    a = None
    b = None

def myview(request):
    o = MyObj()
    o.a = 10
    o.b = "terefere"


    ctx = {"name": "Han Solo",
           "occupation": "smuggler",
           "bool": False,
           "number": 3,
           "mylist": ["Fajny produkt 10/10", "Beznadzieja, nie kupować!", "może być"],
           "my_dict": {"ship": "Millenium Falcon", "owner": "Han Solo"} 
          }
    return render(request, "jedi.html", ctx)

def test(request):
    return render(request, "jedi.html")



class StudentView(View):

    def get(self, request, student_id):

        student = get_object_or_404(Student, pk=student_id)
        subjects = SchoolSubject.objects.all()

        return render(request, "student.html", {"student": student,
                                                "subjects": subjects})


class GradesView(View):

    def get(self, request, student_id, subject_id):

        student = get_object_or_404(Student, pk=student_id)
        subject = get_object_or_404(SchoolSubject, pk=subject_id)

        grades = StudentGrades.objects.filter(student=student,
                                              school_subject=subject)

        average = grades.aggregate(Avg("grade"))

        ctx = {
            "student": student,
            "subject": subject,
            "grades": grades,
            "avg": average
        }
        return render(request, "grades.html", ctx)


class LoginView(View):

    def get(self, request):
        form = NameForm(initial={"login": "admin"})
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            # zrób coś
            login = form.cleaned_data["login"]
            return HttpResponse("login to:" + str(login))
        else:
            return render(request, "login.html", {"form": form})


class StudentSearchView(View):

    def get(self, request):
        form = StudentSearchForm()
        return render(request, "search.html", {"form": form})

    def post(self, request):
        form = StudentSearchForm(request.POST)
        if form.is_valid():
            surname = form.cleaned_data["surname"]
            students = Student.objects.filter(last_name__icontains=surname)
            return render(request, "results.html", {"students": students})


# class AddStudentView(View):

#     def get(self, request):
#         form = AddStudentForm()
#         return render(request, "login.html", {"form": form})

#     def post(self, request):
#         form = AddStudentForm(request.POST)
#         if form.is_valid():
#             student = Student.objects.create(first_name=form.cleaned_data["first_name"],
#                                              last_name=form.cleaned_data["last_name"],
#                                              school_class=int(form.cleaned_data["school_class"]))
#             return redirect("/student/" + str(student.id))
#         else:
#             return render(request, "login.html", {"form": form})

# class AddStudentView(FormView):
#     form_class = AddStudentForm
#     template_name = "login.html"
#     success_url = "/"

class AddStudentView(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'school_class']
    success_url = "/"


class AdditionalIngredientsView(View):

    def get(self, request):
        t = Topping.objects.get(pk=1)
        form = ToppingForm(instance=t)
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = ToppingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("zapisano")
        else:
            return render(request, "login.html", {"form": form})           


class ClassPresenceView(View):

    def get(self, request, student_id, date):
        form = PresenceListForm(initial={"day": date,
                                         "student": student_id})

        return render(request, "login.html", {"form": form})

    def post(self, request, student_id, date):
        form = PresenceListForm(request.POST)
        if form.is_valid():
            student = Student.objects.get(pk=form.cleaned_data["student"])
            pl = PresenceList.objects.create(student=student,
                                             day=form.cleaned_data["day"],
                                             present=form.cleaned_data["present"])

            return HttpResponse("Obecny!")


class UserView(View):

    def get(self, request):
        form = UserForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponse("Przesłano!")
        else:
            return render(request, "login.html", {"form": form})



# todo EGZAMIN
# zad. 2
# jest model dodać 2 model zrobic relacje miedzy modelami i wycagnac relacje które będą wyśietlane
#
# zad. 3
# formularz który trzeba udostepnic w urls widok który obsłurzy ten formularz
#
# zad. 4
# zadanie na kontrole dostepu
#
# zad. 5
# automatyczny admin


# User.objects.create_user('zwykly', 'zwykly@zwykly.pl', 'latwe1234')







from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.core.exceptions import ValidationError

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views import View

from .forms import UserLoginForm, UserCreateForm, ChangePassUserForm, NoticeCreateForm
from .models import Notice



class ListUsersView(LoginRequiredMixin, View):
	'''
	Wymagana jest autentyfikacja, niezalogowany użytkownik zostanie przekierowany
	tam gdzie kieruje LOGIN_URL  (patrz: settings.py)
	'''
	def get(self, request):
		users = User.objects.all()
		return render(request, 'list_users.html', locals())


class LoginUserView(View):
	'''
	Logowanie powinno być dostępne dla wszystkich.
	'''
	def get(self, request):
		form = UserLoginForm()
		return render(request, 'login.html', locals())

	def post(self, request):
		form = UserLoginForm(request.POST)
		if (form.is_valid()):
			u = authenticate(username=form.cleaned_data['username'],
				password=form.cleaned_data['password'])
			if u is not None:
				login(request, u)
				return HttpResponseRedirect("/list_users")

		return render(request, 'login.html', locals())

class LogoutUserView(LoginRequiredMixin, View):
	'''
	Wylogowanie nie ma sensu dla niezalogowanych, więc to sprawdzamy
	przez użycie LoginRequiredMixin
	'''
	def get(self, request):
		# wyczyszenie sesji użytkownika
		logout(request)

		# tutaj ciekawa sprawa, nastąpi przekierowanie do widoku, który
		# wymaga zalogowania, więc możemy sobie wyobrazić, że ostatecznie
		# użytkownik i tak wyląduje tam, gdzie wskazuje LOGIN_URL z settings.py
		return HttpResponseRedirect("/list_users")

from django.contrib.auth.description import login_required
from django.contrib.auth.description import permission_required

@login_required
@permission_required("exercises.add_school")
class AddUserView(PermissionRequiredMixin, FormView):
	'''
	Dla uproszczenia - zezwalamy każdemu dodać użytkownika.
	'''
	template_name = 'add_user.html'
	form_class = UserCreateForm
	success_url = '/list_users'
	permission_required = "auth.change_user"

	def form_valid(self, form):
		# dodawanie
		u = User()
		u.username   = form.cleaned_data['username']
		u.first_name = form.cleaned_data['first_name']
		u.last_name  = form.cleaned_data['last_name']
		u.email      = form.cleaned_data['email']
		u.set_password(form.cleaned_data['password1'])
		u.save()

		return super(AddUserView, self).form_valid(form)


class ChangePassUserView(PermissionRequiredMixin, FormView):
	# to ustawienie powoduje, że praktyce tylko superużytkownik będzie mógł tutaj wejść.
	permission_required = 'auth.change_user'

	template_name = 'add_user.html'
	form_class = ChangePassUserForm
	success_url = '/list_users'

	def form_valid(self, form):
		user_id = self.args[0]
		u = User.objects.get(pk = user_id)
		u.set_password(form.cleaned_data['password1'])

		return super(ChangePassUserView, self).form_valid(form)


class AddNoticeView(PermissionRequiredMixin, FormView):
	# tutaj wg instrukcji osoby z grupy teachers mają uprawnienia,
	# ale ponieważ grupa ma uprawnienie 'users.check_student_timesheet'
	# to użytkownicy znajdujący się w tej grupie mają wjazd
	permission_required = 'users.check_student_timesheet'
	template_name = 'add_user.html'
	form_class = NoticeCreateForm
	success_url = '/list_users' # tutaj właściwsze byłoby list_notices, ale trzeba takie coś zbudować ;)

	def form_valid(self, form):
		n = Notice()
		n.description = form.cleaned_data['description']
		n.save()

		return super(AddNoticeView, self).form_valid(form)

'''
def list_users(request):
    users = User.objects.all()

    return render(request, 'list_users.html', locals())

@permission_required('change_user')
def ulogin(request):
	if request.POST:
		# def post(request)
		form = UserLoginForm(request.POST)
		if (form.is_valid()):
			u = authenticate(username=form.cleaned_data['username'],
				password=form.cleaned_data['password'])
			if u is not None:
				#user = User.objects.get(username = form.cleaned_data['username'])
				login(request, u)
	else:
		# def get(request)
		form = UserLoginForm()
	return render(request, 'login.html', locals())


def ulogout(request):
	logout(request)
	return HttpResponseRedirect("/login")
'''



























