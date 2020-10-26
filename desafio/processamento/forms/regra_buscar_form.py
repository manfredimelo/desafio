from django import forms

CAMPO_CHOICES = (
                ('', '------------'),
                ('cor', 'cor'),
                ('tipo', 'tipo')
              )

class RegraBuscarForm(forms.Form):
    form_control_class = 'form-control '

    campo = forms.ChoiceField(choices=CAMPO_CHOICES, required=False)
    valor = forms.CharField(widget=forms.TextInput(), required=False)


    def __init__(self, *args, **kwargs):
        super(RegraBuscarForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = self.form_control_class
