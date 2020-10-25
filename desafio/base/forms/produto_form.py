from django import forms

from base.models import Produto


class ProdutoForm(forms.ModelForm):
    error_css_class = 'is-invalid '
    success_css_class = 'is-valid '
    form_control_class = 'form-control '
    selectize_class = 'selectize '
    msg_campo_obrigatorio = 'Este campo é obrigatório.'

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


    class Meta:
        model = Produto
        # fields = '__all__'
        exclude = ['processado',]