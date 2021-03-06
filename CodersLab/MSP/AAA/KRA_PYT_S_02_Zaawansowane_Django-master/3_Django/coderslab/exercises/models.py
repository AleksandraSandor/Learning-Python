from django.db import models


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


class PresenceList(models.Model):
    student = models.ForeignKey(Student)
    day = models.DateField()
    present = models.NullBooleanField()


PIZZA_SIZES =   (
                (1, "small"),
                (2, "medium"),
                (3, "big"),
)


class Topping(models.Model):
    name = models.CharField(max_length=32, verbose_name="nazwa")
    price = models.FloatField(verbose_name="cena")


class Pizza(models.Model):
    size = models.IntegerField(choices=PIZZA_SIZES)
    toppings = models.ManyToManyField(Topping)
