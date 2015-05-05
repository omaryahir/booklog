# -*- coding: utf-8 -*-

from django import forms
from .models import Book
from django.core.mail import send_mail

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
        ("Seleccione", "Seleccione"),
        ("Dudas", "Dudas"),
        ("Aclaraciones", "Aclaraciones"),
        ("Contacto", "Contacto"),
        ("Legal", "Legal"))
    asunto = forms.ChoiceField(choices=options, required=True, initial=options[0])
    correo = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea(
                attrs={'placeholder':"Escriba su mensaje"}))

    login = forms.CharField()
    pwd = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        # Method fo custom validation for ALL THE FORM 
        cleaned_data = super(ContactForm, self).clean()
        asunto = cleaned_data.get('asunto')
        if asunto=="Seleccione":
            raise forms.ValidationError("Debe seleccionar un valor de la lista")
        return cleaned_data

    
    def clean_asunto(self):
        # Method for custom validation for ONLY 'asunto' FIELD
        asunto = self.cleaned_data['asunto']
        if asunto=="Seleccione":
            raise forms.ValidationError("Debe seleccionar un valor de la lista")
        return asunto
    
    def send_mail(self):
        # Method for send mail
        cleaned_data = self.clean()
        if cleaned_data.get('asunto') and \
           cleaned_data.get('correo') and \
           cleaned_data.get('mensaje'):
            asunto = cleaned_data.get('asunto')
            correo = cleaned_data.get('correo')
            mensaje = cleaned_data.get('mensaje')
            login = cleaned_data.get('login')
            pwd = cleaned_data.get('pwd')
            
            send_mail(asunto, mensaje, login, [correo],
                        auth_user=login, auth_password=pwd)
            
