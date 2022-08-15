from datetime import datetime
import pytz

from django.db.models import Count, Max, Min, Sum, F, Q, When, Subquery


from import_export import resources
from import_export.fields import Field
from prd.models import Productos
from .models import SolicitudPedido



class PedidosResource(resources.ModelResource):

    fecha_creacion = Field(
        attribute='fecha_creacion',
        column_name='Fecha Creacion'
    )
    descripcion = Field(
        attribute='descripcion',
        column_name='Descripcion'
    )
    
    estado = Field(
        attribute='estado',
        column_name='Estado'
    )

    proveedor = Field(
        column_name="Proveedores"
    )

    fecha_envio = Field(
        attribute="fecha_envio",
        column_name='Fecha Envio a Proveedor'
    )
    fecha_envio = Field(
        attribute="fecha_recibida",
        column_name='Fecha de Recepcion d Insumos'
    )
    total_envio = Field(
        attribute="total_envio",
        column_name='Cantidad de Insumos Solicitados'
    )




    class Meta:
        model = SolicitudPedido
        fields = (
            'fecha_creacion', 'descripcion', 'estado', 'proveedor',
            'fecha_envio', 'fecha_recibida'
        )




    def dehydrate_proveedor(self, SolicitudPedido): 
        nombre_proveedor = '----'
        proveedor = SolicitudPedido.proveedor_id
        if proveedor is not None:
            nombre_proveedor = SolicitudPedido.proveedor.nombres
        return nombre_proveedor