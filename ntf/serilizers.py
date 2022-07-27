from rest_framework import serializers

from ntf.models import *

class NotificacionSerializer(serializers.ModelSerializer):
    descripcion_bodega = serializers.SerializerMethodField()
    class Meta:
        model = Notificacion
        fields = '__all__'

    def get_descripcion_bodega(self, obj):
        tipo_orden = obj.orden
        descripcion = ''
        if tipo_orden:
            descripcion = obj.orden.tipo.descripcion
        return descripcion
       