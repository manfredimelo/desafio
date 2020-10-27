from django.test import TestCase

from base.forms.produto_form import ProdutoForm


class ProdutoFormTest(TestCase):

    def test_form_nome_field_label(self):
        form = ProdutoForm()
        self.assertTrue(
            form.fields['nome'].label == 'Nome')
    def test_form_cor_field_label(self):
        form = ProdutoForm()
        self.assertTrue(
            form.fields['cor'].label == 'Cor')
    def test_form_tipo_field_label(self):
        form = ProdutoForm()
        self.assertTrue(
            form.fields['tipo'].label == 'Tipo')

    def test_form_codigo_gtin_field_label(self):
        form = ProdutoForm()
        self.assertTrue(
            form.fields['codigo_gtin'].label == 'Código')


    def test_form_codigo_gtin_field_help_text(self):
        form = ProdutoForm()
        self.assertEqual(form.fields['codigo_gtin'].help_text, 'Código Único')


