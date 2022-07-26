from rest_framework import serializers

from personal.models import CategoriaPersonal, PersonalFinca

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriaPersonal
        fields = '__all__'

class PersonalSerializers(serializers.ModelSerializer):
    tipo_descripcion = serializers.CharField(source="tipo.descripcion")
    categoria_descripcion = serializers.CharField(source="categoria.descripcion")

    class Meta:
        model = PersonalFinca
        fields = '__all__'