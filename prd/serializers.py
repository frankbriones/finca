from rest_framework import serializers

from prd.models import *

class ProductosSerializer(serializers.ModelSerializer):
    categoria_descripcion = serializers.CharField(source='categoria.descripcion')
    unidad_medida_descripcion = serializers.CharField(source='unidad_medida.descripcion')
    
    class Meta:
        model = Productos
        fields = '__all__'