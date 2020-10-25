# -*- coding: utf-8 -*-
u"""."""

from django.contrib import admin

from processamento.models import Regra, Classificacao

admin.site.register(Regra)
admin.site.register(Classificacao)