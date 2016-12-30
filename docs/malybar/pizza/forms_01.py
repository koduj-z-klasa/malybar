# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from .models import Pizza, Skladnik
from django.forms.models import inlineformset_factory


class PizzaForm(ModelForm):

    class Meta:
        model = Pizza
        fields = ('nazwa', 'opis', 'rozmiar', 'cena')
        exclude = ('data', 'autor')
        widgets = {'opis': Textarea(attrs={'rows': 2, 'cols': 80})}


SkladnikiFormSet = inlineformset_factory(
    Pizza, Skladnik,
    max_num=6,
    min_num=1,
    validate_max=True,
    validate_min=True,
    extra=2,
    can_delete=True,
    fields=('nazwa', 'jarski')
)
