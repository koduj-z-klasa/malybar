Wycięte

	- :file:`urls.py` – plik, który dopiero utworzymy, będzie zawierał listę adresów i związanych z nimi widoków.

Znak ``^`` rozpoczyna wyrażenie, a ``$`` kończy. Wyrażenie ``r'^$'`` oznacza
adres podstawowy. W praktyce jest to nazwa serwera (domenowa lub w formie adresu IP) z ewentualnym portem, np.
adres serwera deweloperskiego ``127.0.0.1:8000``.

.. note::

	Wyrażenia, których zadaniem jest zaimportowanie innych konfiguracji, kończą się zazwyczaj znakiem ``/``.

	Typowe błędy w kodowaniu
	[todo]

 wykorzystując wbudowany system ORM (ang.). służący zarówno do definiowania,
jak i zarządzania źródłami danych.

  ~/dj_10_4/malybar$ python manage.py sqlmigrate pizza 0001

Testowanie modelu
-----------------

Po zdefiniowaniu modelu możemy go od przetestować w konsoli, zanim wykorzystamy
go w aplikacji.

.. code-block:: bash

  ~/dj_10_4/malybar$ python manage.py shell

Powyższe polecenie uruchamia konsolę Pythona (rozszerzoną, jeżeli jest dostępna) i tworzy
środowisko testowe. Zobaczmy, jak za pomocą bazodanowego API zarządzać danymi.

**Dodawanie danych** (ang. *create*):

.. code-block:: bash

	>>> from pizza.models import *
	>>> margarita = Pizza(nazwa="Margarita", cena="22.99")
	>>> margarita.save()
	>>> margarita.id, margarita.nazwa, margarita.cena
	>>> serowa = Pizza.objects.create(nazwa="serowa", cena="19.99")
	>>> ser = Skladnik(margarita, nazwa="ser")
	>>> ser.save()
	>>> pieczarki = Skladnik(margarita, nazwa="pieczarki")
	>>> pieczarki.save()

**Odczytywanie danych** (ang. *read*) z bazy:

.. code-block:: bash

	>>> from django.utils import timezone
	>>> pizze = Pizza.objects.all()
	>>> print pizze
	>>> print pizze[0].id, pizze[0].nazwa, pizze[0].data
	>>> pizza = Pytanie.objects.get(pk=1)
	>>> print pizza.nazwa
	>>> Pizza.objects.filter(data__year=timezone.now().year)
	>>> Pizza.objects.filter(nazwa__startswith='M')
	>>> Pizza.objects.count()

admin.py:

# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Pizza, Skladnik
from django.forms import Textarea
from django.db import models


class SkladnikInline(admin.TabularInline):
    model = Skladnik
    max_num = 6
    extra = 3
    fields = ['nazwa', 'jarski']


class PizzaAdmin(admin.ModelAdmin):
    # fields = ['przedmiot', 'kategoria', 'typ', 'polecenie']
    exclude = ('autor',)
    # obiekty zależne do wyświetlenia
    inlines = [SkladnikInline]
    # nagłówki do wyświetlenia
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    # wyszukiwanie
    search_fields = ['nazwa']
    list_per_page = 10

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})},
    }

    def save_model(self, request, obj, form, change):
        if not change:
            obj.autor = request.user
        obj.save()


# rejestrujemy model Pizza w panelu administracyjnym
admin.site.register(Pizza, PizzaAdmin)

