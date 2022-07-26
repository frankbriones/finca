from rest_framework import serializers

from ubc.models import *

class SeccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secciones
        fields = '__all__'