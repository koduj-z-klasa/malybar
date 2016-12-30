# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Pizza, Skladnik

# rejestrujemy modele w panelu administracyjnym
admin.site.register(Pizza)
admin.site.register(Skladnik)
