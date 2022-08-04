from rest_framework import serializers

from prd.models import *

class ProductosSerializer(serializers.ModelSerializer):
    categoria_descripcion = serializers.CharField(source='categoria.descripcion')
    seccion_descripcion = serializers.CharField(source='seccion.descripcion')
    unidad_medida_descripcion = serializers.CharField(source='unidad_medida.descripcion')
    
    class Meta:
        model = Productos
        fields = '__all__'



class CategoriaProductoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = CategoriaProducto
        fields = [
            'id_categoria',
            'descripcion'
        ]