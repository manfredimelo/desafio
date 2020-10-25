# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import PROTECT
from base.models.produto import Produto
from processamento.models.regra import Regra


class Classificacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=PROTECT)
    regra = models.ForeignKey(Regra, on_delete=PROTECT)
    resultado = models.BooleanField(verbose_name='Resultado',
                                         default=False)
    class Meta():
        app_label = 'processamento'

    def __unicode__(self):
        return u'%s ' % (self.produto)