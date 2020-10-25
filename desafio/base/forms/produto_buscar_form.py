from django import forms
from base.models import Produto

PROCESSADOS_CHOICES = [
    ('', '--------'),
    ('SIM', 'SIM'),
    ('NAO', 'NÃO'),
]


class ProdutoBuscarForm(forms.Form):
    form_control_class = 'form-control '
    nome = forms.CharField(widget=forms.TextInput(), required=False)
    tipo = forms.CharField(widget=forms.TextInput(), required=False)
    cor  = forms.CharField(widget=forms.TextInput(), required=False)
    processado = forms.ChoiceField(choices=PROCESSADOS_CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super(ProdutoBuscarForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = self.form_control_class
