from django import forms

class SumaForm(forms.Form):
    valor1 = forms.IntegerField(label='El valor 1')
    valor2 = forms.IntegerField(label='El valor 2')
    valor3 = forms.IntegerField()


class
