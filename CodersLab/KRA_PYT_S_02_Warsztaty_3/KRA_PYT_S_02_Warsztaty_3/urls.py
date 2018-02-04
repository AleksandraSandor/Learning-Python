"""KRA_PYT_S_02_Warsztaty_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from KRA_PYT_S_02_Warsztaty_3_app.views.contact_list_view import ContactListView
from KRA_PYT_S_02_Warsztaty_3_app.views.contact_add_view import ContactAddView
from KRA_PYT_S_02_Warsztaty_3_app.views.landing_view import LandingView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact/list$', ContactListView.as_view()),
    url(r'', LandingView.as_view()),
    url(r'^contact/add$', ContactAddView.as_view()),
]


