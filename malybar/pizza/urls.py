# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views  # import widoków aplikacji
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import Pizza

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lista/', login_required(ListView.as_view(model=Pizza)),
        name='lista'),
    url(r'^dodaj/$', views.PizzaCreate.as_view(), name='dodaj'),
    url(r'^edytuj/(?P<pk>\d+)/', views.PizzaUpdate.as_view(), name='edytuj'),
    url(r'^usun/(?P<pk>\d+)/', views.PizzaDelete.as_view(), name='usun'),
    url(r'^info/(?P<pk>\d+)/', views.PizzaDetailView.as_view(), name='info'),
]
