# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models
from django.forms import Textarea
from django.db.models.fields import TextField


class SkladnikInline(admin.TabularInline):
    model = models.Skladnik
    fields = ['nazwa', 'jarski']
    extra = 3
    max_num = 6


@admin.register(models.Pizza)
class PizzaAdmin(admin.ModelAdmin):
    exclude = ('autor',)
    inlines = [SkladnikInline]
    search_fields = ['nazwa']
    list_per_page = 10
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})},
    }

    def save_model(self, request, obj, form, change):
        if not change:
            obj.autor = request.user
        obj.save()
