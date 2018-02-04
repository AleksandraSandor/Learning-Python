"""django_first URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django_1.views import (add_product, add_product_small, get_product, all_product, get_product_by_name,
                            get_product_by_name_and_id, get_by_price, filter_description, some_id, modify_product,
                            add_opinions, get_opinions, add_opinion, add_discount, get_discount, add_order, get_order,
                            det_order_by_id, get_order_by_product_id, calculate_power_2, zad_1, tabliczka,
                            login_form, hello_1, temp, login_form_session, login_out, setSession, showSession,
                            deleteSession, login, addToSession, showAllSession, session_clear, session_print,
                            session_add_form, cookie_set, cookie_get, cookie_print, cookie_add_form, cookie_clear,
                            set_as_favourite, mojastrona) # delete_from_order
from django_2.views import hello
from django_3.views import (losowa, show_number_with_max, show_number_with_min_max, show_name)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^index/(?P<number>(\d)+)$',	show_number),
    url(r'^hello$', hello),
    url(r'^random$', losowa),
    url(r'^random/(?P<max_num>(\d)+)$', show_number_with_max),
    url(r'^random/(?P<min_num>(\d)+)/(?P<max_num>(\d)+)$', show_number_with_min_max),
    url(r'^hello/(?P<name>([A-Za-z])+)$', show_name),
    url(r'^add_product$',add_product),
    url(r'^add_product_small$',add_product_small),
    url(r'^get_product/(?P<id_prod>([A-Za-z])+)$',get_product),
    url(r'^all_product$',all_product),
    url(r'^get_product_by_name/(?P<price>(\d)+)$',get_product_by_name),
    url(r'^get_product_by_name_and_id/(?P<price>(\d)+)/(?P<name_my>([A-Za-z])+)$',get_product_by_name_and_id),
    url(r'^all_by_price/(?P<price>(\d)+)$', get_by_price),
    url(r'^filter_description/(?P<name_my>([A-Za-z])+)$',filter_description),
    url(r'^some_id/(?P<id_1>(\d)+)/(?P<id_2>(\d)+)$',some_id),
    url(r'^modify_product/(?P<id_1>(\d)+)/(?P<new_price>(\d)+)$',modify_product),
    url(r'^add_opinions/', add_opinions),
    url(r'^get_opinions/', get_opinions),
    url(r'^add_opinion/(?P<id_my>(\d)+)/(?P<description>([A-Za-z])+)$',add_opinion),
    url(r'^add_discount/', add_discount),
    url(r'^get_discount/', get_discount),
    url(r'^add_order/', add_order),
    url(r'^get_order/', get_order),
    url(r'^det_order_by_id/(?P<my_id>(\d)+)$',det_order_by_id),
    #url(r'^delete_from_order/(?P<order_id>(\d)+)/(?P<prod>([A-Za-z])+)$', delete_from_order),
    url(r'^get_order_by_product_id/', get_order_by_product_id),
    url(r'^calculate_power_2/',calculate_power_2),
    url(r'^zad_1/',zad_1),
    url(r'^tabliczka/',tabliczka),
    url(r'^login_form/',login_form),
    url(r'^hello_1/',hello_1),
    url(r'^temp/',temp),
    url(r'^login_form_session/',login_form_session),
    url(r'^login_out/',login_out),
    url(r'^setSession/',setSession),
    url(r'^showSession/',showSession),
    url(r'^deleteSession/',deleteSession),
    url(r'^login/',login),
    url(r'^addToSession/',addToSession),
    url(r'^showAllSession/',showAllSession),
    url(r'^session_clear/',session_clear),
    url(r'^session_print/',session_print),
    url(r'^session_add_form/',session_add_form),
    url(r'^cookie_set/',cookie_set),
    url(r'^cookie_get/',cookie_get),
    url(r'^cookie_print/',cookie_print),
    url(r'^cookie_add_form/',cookie_add_form),
    url(r'^cookie_clear/',cookie_clear),
    url(r'^set_as_favourite/(?P<my_id>(\d)+)$',set_as_favourite),
    url(r'^mojastrona/(?P<nazwa>[a-z]+)$',mojastrona)   #todo RAFALA to NIE jest GET !!!
]