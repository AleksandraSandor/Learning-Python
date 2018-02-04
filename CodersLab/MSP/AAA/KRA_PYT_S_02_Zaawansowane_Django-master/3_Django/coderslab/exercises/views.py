from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.edit import FormView, CreateView

from .models import (SCHOOL_CLASS, Student, SchoolSubject, StudentGrades,
                     PresenceList, Topping)

from .forms import (NameForm, StudentSearchForm, AddStudentForm,
                    ComposePizzaForm, PresenceListForm, UserForm, ToppingForm)

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
