from django import forms

from processamento.models import Regra


CAMPO_CHOICES = (
                ('cor', 'cor'),
                ('tipo', 'tipo')
              )

class RegraForm(forms.ModelForm):
    error_css_class = 'is-invalid '
    success_css_class = 'is-valid '
    form_control_class = 'form-control '
    selectize_class = 'selectize '
    msg_campo_obrigatorio = 'Este campo é obrigatório.'

    campo = forms.ChoiceField(choices=CAMPO_CHOICES, required=False)
    def __init__(self, *args, **kwargs):
        super(RegraForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


    class Meta:
        model = Regra
        fields = '__all__'
