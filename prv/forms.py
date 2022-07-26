from xml.dom.minidom import Identified
from django import forms

from django import forms
from django.forms.widgets import TextInput, EmailInput, FileInput,  NumberInput, Textarea

from .models import *
from ubc.models import *
from usr.models import Usuarios

class ProveedoresForm(forms.Form):
    identificacion = forms.CharField(max_length=10)
    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    telefono = forms.CharField(
       widget=forms.TextInput(),
       max_length=10,
       label='Movil'
       )
    correo = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )
    direccion = forms.CharField(max_length=100)
    ciudad = forms.ModelChoiceField(queryset=Ciudades.objects.all(),empty_label="--Escoger Ciudad--")
    usuario = forms.CharField(max_length=100)

    
    # class Meta:
    #     model = Proveedores
    #     fields = [
    #         'identificacion',
    #         'nombres',
    #         'apellidos',
    #         'telefono',
    #         'correo',
    #         'direccion',
    #         'ciudad',
    #         #'categoria'
    #     ]
    #     widgets = {
    #         'correo': forms.TextInput(attrs={ 'placeholder':'example@mail.com', 'type':'email'}),
    #     }
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    def clean_correo(self):
        correo_prv = self.cleaned_data.get('correo')
        if(len(correo_prv) < 3):
            raise forms.ValidationError('Correo no valido')



# class SignupForm(forms.Form):
#    """Sign up form."""
#    nombres = forms.CharField(min_length=2, max_length=50, label= 'Nombres')
#    apellidos = forms.CharField(min_length=2, max_length=50, label= 'Apellidos')
#    email = forms.CharField(
#        min_length=6,
#        max_length=70,
#        widget=forms.EmailInput()
#   )
#    password = forms.CharField(
#        max_length=70,
#        widget=forms.PasswordInput(),
#        help_text=password_validation.password_validators_help_text_html(),
#    )
#    password_confirmation = forms.CharField(
#        max_length=70,
#        widget=forms.PasswordInput(),
#        label='Confirmacion de Password'
#    )

#    celular = forms.CharField(
#        widget=forms.TextInput(),
#        max_length=10,
#        label='Movil'