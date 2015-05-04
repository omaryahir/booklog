# -*- coding: utf-8 -*-

from django import forms
from .models import Book

class SumaForm(forms.Form):
    valor1 = forms.IntegerField(label='El valor 1')
    valor2 = forms.IntegerField(label='El valor 2')
    valor3 = forms.IntegerField()

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class ContactForm(forms.Form):
    # TODO: Formulario de contacto
    options = (
        ("", "-------"),
        ("Seleccione", "Seleccione"),
        ("Dudas", "Dudas"),
        ("Aclaraciones", "Aclaraciones"),
        ("Contacto", "Contacto"),
        ("Legal", "Legal"))
    asunto = forms.ChoiceField(choices=options, required=True, initial=options[0])
    correo = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea(
                attrs={'placeholder':"Escriba su mensaje"}))


