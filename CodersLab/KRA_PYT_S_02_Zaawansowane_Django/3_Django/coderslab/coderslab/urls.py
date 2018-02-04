"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from exercises.views import (SchoolView, SchoolClassView,
                             myview, test,
                             StudentView, GradesView, LoginView,
                             StudentSearchView, AddStudentView,
                             AdditionalIngredientsView, ClassPresenceView,
                             UserView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', SchoolView.as_view(), name="index"),
    url(r'^class/(?P<school_class>(\d)+)', SchoolClassView.as_view(), 
         name="school-class" ),

    url(r'^student/(?P<student_id>(\d)+)', StudentView.as_view(), name="student"),
    url(r'^grades/(?P<student_id>(\d)+)/(?P<subject_id>(\d)+)', GradesView.as_view(), name="grades"),
    

    url(r'^jedi/', myview, name="jedi"),
    url(r'^terefere', test),
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^student_search/', StudentSearchView.as_view(), name="search"),
    url(r'^add_student/', AddStudentView.as_view(), name="add_student"),
    url(r'^compose_pizza/', AdditionalIngredientsView.as_view(),
        name="compose_pizza"),

    url(r'^class_presence/(?P<student_id>(\d)+)/(?P<date>(\d){4}-(\d){2}-(\d){2})/', 
        ClassPresenceView.as_view(), 
        name="presence"),

    url(r'^d2_p3_e1/', UserView.as_view(), name="user_view")
    
    
    
    # url(r'^list_users/', users_views.ListUsersView.as_view(), name='userslist'),
    # url(r'^login/', users_views.LoginUserView.as_view()),
    # url(r'^logout/', users_views.LogoutUserView.as_view()),
    #
    # url(r'^add_user/', users_views.AddUserView.as_view(), name='adduser'),
    # url(r'^change_pass/([0-9]+)/', users_views.ChangePassUserView.as_view(),
    #     name='changepass'),
    #
    # url(r'^add_notice/', users_views.AddNoticeView.as_view(),
    #     name='addnotice'),
    
    
    
    
    

]
