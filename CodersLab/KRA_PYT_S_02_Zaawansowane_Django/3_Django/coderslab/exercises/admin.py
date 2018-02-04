from django.contrib import admin

# Register your models here.

from .models import Student, StudentGrades, SchoolSubject, PresenceList, Topping, Pizza, Notice, Author, Book, Tag

@admin.register(Student)
class Student(admin.ModelAdmin):
	pass

@admin.register(StudentGrades)
class StudentGrades(admin.ModelAdmin):
	pass

@admin.register(SchoolSubject)
class SchoolSubject(admin.ModelAdmin):
	pass

@admin.register(PresenceList)
class PresenceList(admin.ModelAdmin):
	pass

@admin.register(Topping)
class Topping(admin.ModelAdmin):
	pass

@admin.register(Pizza)
class Pizza(admin.ModelAdmin):
	pass

@admin.register(Notice)
class Notice(admin.ModelAdmin):
	pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ("first_name", "last_name")
	
def set_book_hire(model_admin, request, query_set):
	query_set.update(is_hired = True)
set_book_hire.short_description = "Oznacz jako wyporzyczone"

def set_book_nohire(model_admin, request, query_set):
	query_set.update(is_hired = False)
set_book_nohire.short_description = "Oznacz jako nie wyporzyczone"

def set_book_cleantags(model_admin, request, query_set):
	for b in query_set:
		b.tag_set.delete()
set_book_cleantags.short_description = "Usuń tag"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	# exclude
	# pass
	list_display = ("title", "genre", "author", "owner", "is_hired", "created", "tag_list" )
	execlude = ["created",]
	actions = [set_book_hire, set_book_nohire, set_book_cleantags ]
	# def get_author_lastname(self, obj):
	# 	return obj.author
	
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ("name",)
	


