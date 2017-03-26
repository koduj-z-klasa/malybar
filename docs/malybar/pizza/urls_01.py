# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views  # import widoków aplikacji

app_name = 'pizza'  # przestrzeń nazw aplikacji
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
