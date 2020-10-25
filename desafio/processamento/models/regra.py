# -*- coding: utf-8 -*-
from django.db import models

class Regra(models.Model):
    campo = models.CharField('Campo', max_length=100)
    valor = models.CharField('Valor', max_length=100)

    class Meta():
        app_label = 'processamento'

    def __unicode__(self):
        return u'%s ' % (self.campo)
