from django.test import TestCase
from processamento.models import Regra


class RegraTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Regra.objects.create(campo='tipo', valor='popular')

    def test_nome_label(self):
        regra = Regra.objects.get(id=1)
        field_label = regra._meta.get_field('campo').verbose_name
        self.assertEquals(field_label, 'Campo')

    def test_valor_label(self):
        regra = Regra.objects.get(id=1)
        field_label = regra._meta.get_field('valor').verbose_name
        self.assertEquals(field_label, 'Valor')

    def test_campo_max_length(self):
        regra = Regra.objects.get(id=1)
        max_length = regra._meta.get_field('campo').max_length
        self.assertEquals(max_length, 100)

    def test_valor_max_length(self):
        regra = Regra.objects.get(id=1)
        max_length = regra._meta.get_field('valor').max_length
        self.assertEquals(max_length, 100)

    def test_valor_url_model(self):
        regra = Regra.objects.get(id=1)
        self.assertEquals(regra.get_absolute_url_regra(), '/regras/editar/1/')



    def test_object_name_is_regra_name(self):
        regra = Regra.objects.get(id=1)
        expected_object_name = str(regra)

        resultado_esperado= str(regra.campo)+': '+str(regra.valor)

        self.assertEquals(expected_object_name, resultado_esperado)

