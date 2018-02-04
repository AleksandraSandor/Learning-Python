from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

SCHOOL_CLASS = (
    (1, "1a"),
    (2, "1b"),
    (3, "2a"),
    (4, "2b"),
    (5, "3a"),
    (6, "3b"),
)

GRADES = (
    (1, "1"),
    (1.5, "1+"),
    (1.75, "2-"),
    (2, "2"),
    (2.5, "2+"),
    (2.75, "3-"),
    (3, "3"),
    (3.5, "3+"),
    (3.75, "4-"),
    (4, "4"),
    (4.5, "4+"),
    (4.75, "5-"),
    (5, "5"),
    (5.5, "5+"),
    (5.75, "6-"),
    (6, "6")
)

# Create your models here.
class SchoolSubject(models.Model):
    name = models.CharField(max_length=64)
    teacher_name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name =  models.CharField(max_length=64)
    school_class = models.IntegerField(choices=SCHOOL_CLASS)
    grades = models.ManyToManyField(SchoolSubject, through="StudentGrades")

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class StudentGrades(models.Model):
    student = models.ForeignKey(Student)
    school_subject = models.ForeignKey(SchoolSubject)
    grade = models.FloatField(choices=GRADES)
    def __str__(self):
        return self.student


class PresenceList(models.Model):
    student = models.ForeignKey(Student)
    day = models.DateField()
    present = models.NullBooleanField()

    def __str__(self):
        return "{} {}".format(self.student.name, str(self.day))

PIZZA_SIZES =   (
                (1, "small"),
                (2, "medium"),
                (3, "big"),
)


class Topping(models.Model):
    name = models.CharField(max_length=32, verbose_name="nazwa")
    price = models.FloatField(verbose_name="cena")
    def __str__(self):
        return self.name


class Pizza(models.Model):
    size = models.IntegerField(choices=PIZZA_SIZES)
    toppings = models.ManyToManyField(Topping)
    def __str__(self):
        return "Pizza ID: {}".format(str(self.id))
    
    
class Message(models.Model):
   subject = models.CharField(max_length=256)
   content = models.TextField()
   to = models.ForeignKey(SchoolSubject)
   fro = models.ForeignKey(Student)
   data_sent = models.DateTimeField(default=datetime.now())


class Notice(models.Model):
    class Meta:
        permissions = (
            ("add_student_notice", "Testowe uprawnienie"),
        )

    description = models.CharField(max_length=100)
    
    
class Author(models.Model):
    class Meta:
        ordering = ("last_name",)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return self.last_name
    
BOOK_GENRE = (
    (1, "kryminał"),
    (2, "romans"),
    (3, "sci-fi/fanstasy/horror"),
    (4, "literatura faktu"),
    (5, "poradnik"),
    (6, "obyczajowa"),
)
class Book(models.Model):
    class Meta:
        ordering = ("title",)
    title = models.CharField(max_length=100, verbose_name = "Tytuł", help_text = "Coś tam coś")
    genre = models.IntegerField(choices=BOOK_GENRE)
    author = models.ForeignKey(Author)
    owner = models.ForeignKey(User)
    is_hired = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    @property
    def tag_list(self):
        return ". ".join([str(t) for t in self.tag_set.all()])

class Tag(models.Model):
    class Meta:
        ordering = ("name", )
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name
 