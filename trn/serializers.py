from rest_framework import serializers

from trn.models import *

class SolicitudSerializer(serializers.ModelSerializer):
    usuario_nombres = serializers.SerializerMethodField()
    nombres_proveedor = serializers.SerializerMethodField()
    apellidos_proveedor = serializers.SerializerMethodField()
    estado_nombre = serializers.CharField(source='estado.descripcion')

    class Meta:
        model = SolicitudPedido
        fields = '__all__'

    def get_usuario_nombres(self, obj):
        usuario_id = int(obj.usuario_crea)
        user_obj = Usuarios.objects.filter(pk=usuario_id).first()
        return user_obj.get_full_name()

    def get_nombres_proveedor(self, obj):
        if obj.proveedor_id != None:
            proveedor_id = int(obj.proveedor_id)
            prv_obj = Proveedores.objects.filter(id_proveedor=proveedor_id).first()
            if prv_obj:
                return prv_obj.nombres
        else:
            return '----------'
    
    def get_apellidos_proveedor(self, obj):
        if obj.proveedor_id != None:
            proveedor_id = int(obj.proveedor_id)
            prv_obj = Proveedores.objects.filter(id_proveedor=proveedor_id).first()
            if prv_obj:
                return prv_obj.apellidos
        else:
            return '----------'


class DetalleSolicitudSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductosSolicitud
        fields = '__all__'


