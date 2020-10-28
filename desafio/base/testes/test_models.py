from django.test import TestCase
from base.models import Produto


class ProdutoTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Produto.objects.create(nome='carro', codigo_gtin='001234', tipo='popular', cor='preto')
    def test_nome_label(self):
        produto = Produto.objects.get(id=1)
        field_label = produto._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'Nome')

    def test_tipo_label(self):
        produto = Produto.objects.get(id=1)
        field_label = produto._meta.get_field('tipo').verbose_name
        self.assertEquals(field_label, 'Tipo')

    def test_codigo_gtin_label(self):
        produto = Produto.objects.get(id=1)
        field_label = produto._meta.get_field('codigo_gtin').verbose_name
        self.assertEquals(field_label, 'Código')

    def test_cor_label(self):
        produto = Produto.objects.get(id=1)
        field_label = produto._meta.get_field('cor').verbose_name
        self.assertEquals(field_label, 'Cor')

    def test_processado_label(self):
        produto = Produto.objects.get(id=1)
        field_label = produto._meta.get_field('processado').verbose_name
        self.assertEquals(field_label, 'Processado')

    def test_nome_max_length(self):
        produto = Produto.objects.get(id=1)
        max_length = produto._meta.get_field('nome').max_length
        self.assertEquals(max_length, 100)

    def test_cor_max_length(self):
        produto = Produto.objects.get(id=1)
        max_length = produto._meta.get_field('cor').max_length
        self.assertEquals(max_length, 100)

    def test_tipo_max_length(self):
        produto = Produto.objects.get(id=1)
        max_length = produto._meta.get_field('tipo').max_length
        self.assertEquals(max_length, 100)

    def test_codigo_gtin_length(self):
        produto = Produto.objects.get(id=1)
        max_length = produto._meta.get_field('codigo_gtin').max_length
        self.assertEquals(max_length, 100)

    def test_get_absolute_url(self):
        produto = Produto.objects.get(id=1)
        self.assertEquals(produto.get_absolute_url(), '/editar_produto/1/')

    def test_object_name_is_procuto_name(self):
        produto = Produto.objects.get(id=1)
        expected_object_name = f'{produto.nome}'
        self.assertEquals(expected_object_name, str(produto.nome))

    def test_object_processado_is_false(self):
        produto = Produto.objects.get(id=1)
        expected_object_processado = produto.processado
        self.assertEquals(expected_object_processado, False)
