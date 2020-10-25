from django import forms



class RegraBuscarForm(forms.Form):
    form_control_class = 'form-control '

    campo = forms.CharField(widget=forms.TextInput(), required=False)
    valor  = forms.CharField(widget=forms.TextInput(), required=False)


    def __init__(self, *args, **kwargs):
        super(RegraBuscarForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = self.form_control_class
