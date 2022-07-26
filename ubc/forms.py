from django import forms
from django.contrib.auth.models import *

from ubc.models import *


class BodegaForm(forms.ModelForm):

    class Meta:
        model = Bodegas
        fields = [
            'descripcion',
            'direccion1',
            'ciudad'
        ]
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })