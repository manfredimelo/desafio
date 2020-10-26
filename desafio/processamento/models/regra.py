# -*- coding: utf-8 -*-
from django.db import models

class Regra(models.Model):
    campo = models.CharField('Campo', max_length=100)
    valor = models.CharField('Valor', max_length=100)

    class Meta():
        app_label = 'processamento'
        unique_together = ['campo', 'valor']

    def get_classificacoes(self):
        classificicacoes = self.classificacao_set.all()

    def __str__(self):
        return u'%s: %s ' % (self.campo, self.valor)
