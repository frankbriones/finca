from django import forms

from trn.models import *


class SolicitudForm(forms.ModelForm):

    class Meta:
        model = SolicitudPedido
        fields = [
            'descripcion',
            'proveedor'
        ]
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class OrdenProduccionForm(forms.ModelForm):

    class Meta:
        model = OrdenProduccion
        fields = [
            'id_solicitud',
            'descripcion',
        ]
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })