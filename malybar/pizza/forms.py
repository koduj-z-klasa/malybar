# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from . import models
from django.forms.models import inlineformset_factory


class PizzaForm(ModelForm):

    class Meta:
        model = models.Pizza
        fields = ('nazwa', 'opis', 'rozmiar', 'cena')
        exclude = ('data', 'autor')
        widgets = {'opis': Textarea(attrs={'rows': 2, 'cols': 80})}


SkladnikiFormSet = inlineformset_factory(
    parent_model=models.Pizza,
    model=models.Skladnik,
    max_num=6,
    min_num=1,
    validate_max=True,
    validate_min=True,
    extra=2,
    can_delete=True,
    fields=('nazwa', 'jarski')
)


class PizzaUpdateForm(ModelForm):

    class Meta:
        model = models.Pizza
        fields = ('nazwa', 'opis', 'rozmiar', 'cena')
        exclude = ('data', 'autor')
        widgets = {'opis': Textarea(attrs={'rows': 2, 'cols': 80})}


# class QuizdAuthForm(AuthenticationForm):

#     def __init__(self, *args, **kwargs):
#         super(QuizdAuthForm, self).__init__(*args, **kwargs)

#         self.base_fields['username'].widget.attrs['class'] = 'form-control'
#         self.base_fields['username'].widget.attrs['placeholder'] = 'Login'

#         self.base_fields['password'].widget.attrs['class'] = 'form-control'
#         self.base_fields['password'].widget.attrs['placeholder'] = 'Hasło'
