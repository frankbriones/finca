from django import forms
from django.contrib.auth.models import *

from prd.models import *
from ubc.models import *


class ProductoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self ).__init__( *args, **kwargs )
        self.request = kwargs.pop('request', None)
        self.fields['bodega'] = forms.ModelChoiceField(queryset = Bodegas.objects.all(),empty_label="Escoger una bodega", 
            widget=forms.Select(attrs={'placeholder':'Bodegas', 'onChange':"getSecciones(this.value)"}))
        self.fields['seccion'] = forms.ModelChoiceField(queryset = Secciones.objects.none(), empty_label="Escoger una seccion")

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def modificarQuerySet(self, bodega_id):
        if bodega_id not in ('', None):
            self.fields['seccion'].queryset = Secciones.objects.filter(bodega_id = bodega_id)

    class Meta:
        model = Productos
        fields = [
            'descripcion',
            'categoria',
            'unidad_medida',
            'cantidad_minima',
            'bodega',
            'seccion',
        ]
    

    def clean_descripcion(self):
        
        descripcion = self.cleaned_data.get("descripcion")
        if Productos.objects.filter(descripcion=descripcion).exists():
            raise forms.ValidationError("Descripcion ya existe.")
        return descripcion

    def clean_categoria(self):
        categoria = self.cleaned_data.get("categoria")
        if categoria is None:
            raise forms.ValidationError("seleccione una categoria.")
        return categoria
    
    def clean_unidad_medida(self):
        unidad_medida = self.cleaned_data.get("unidad_medida")
        if unidad_medida is None:
            raise forms.ValidationError("seleccione unidad de medida.")
        return unidad_medida

    def clean_bodega(self):
        bodega = self.cleaned_data.get("bodega")
        print(bodega)
        if bodega is None or bodega == '':
            raise forms.ValidationError("seleccione una bodega.")
        return bodega

    def clean_seccion(self):
        seccion = self.cleaned_data.get("seccion")
        print(seccion)
        if seccion is None:
            raise forms.ValidationError("seleccione la seccion donde se almacenara el insumo.")
        return seccion

    def clean_proveedor(self):
        proveedor = self.cleaned_data.get("proveedor")
        if proveedor is None:
            raise forms.ValidationError("seleccione al proveedor del insumo.")
        return proveedor