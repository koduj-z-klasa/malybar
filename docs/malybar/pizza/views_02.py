# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from . import forms
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


def index(request):
    """Strona główna"""
    kontekst = {'komunikat': 'Witaj w aplikacji Pizza!'}
    return render(request, 'pizza/index.html', kontekst)


@method_decorator(login_required, 'dispatch')
class PizzaCreate(CreateView):
    """Widok dodawania pizzy i skladników."""

    model = models.Pizza
    form_class = forms.PizzaForm
    success_url = reverse_lazy('pizza:lista')  # '/pizza/lista'

    def get_context_data(self, **kwargs):
        context = super(PizzaCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['skladniki'] = forms.SkladnikiFormSet(self.request.POST)
        else:
            context['skladniki'] = forms.SkladnikiFormSet()
        return context

    def form_valid(self, form):
        form.instance.autor = self.request.user
        context = self.get_context_data()
        skladniki = context['skladniki']
        if form.is_valid() and skladniki.is_valid():
            self.object = form.save()
            skladniki.instance = self.object
            skladniki.save()
            return HttpResponseRedirect(self.get_success_url())
        return self.form_invalid(form, skladniki)

    def form_invalid(self, form, skladniki):
        errors = skladniki.non_form_errors()
        if skladniki.total_form_count() == 0:
            skladniki = forms.SkladnikiFormSet()
            skladniki._non_form_errors = errors
        return self.render_to_response(
            self.get_context_data(form=form, skladniki=skladniki)
        )
