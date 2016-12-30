# -*- coding: utf-8 -*-

from django.shortcuts import render


def index(request):
    """Strona główna"""
    kontekst = {'komunikat': 'Witaj w aplikacji Pizza!'}
    return render(request, 'pizza/index.html', kontekst)
