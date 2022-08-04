from django.db import models

# Create your models here.
from bases.models import ClaseModelo, Estados
from usr.models import Usuarios
from prv.models import Proveedores
from prd.models import Productos



from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

#modelo de solicitu a proveedores
class SolicitudPedido(ClaseModelo):
    id_solicitud = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=500)
    secuencia = models.CharField(max_length=20, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, blank=True, null=True)
    fecha_envio = models.DateTimeField(blank=True, null=True)
    fecha_recibida = models.DateTimeField(blank=True, null=True)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, blank=True, null=True )
    total_envio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)

    class Meta:
        permissions = {
            ('crear_orden_proveedor', ('Crear Orden a Proveedores')),
            ('ver_ordenes_proveedor', ('Ver ordenes de Proveedores')),
            ('actualizar_ordenes_proveedor', ('Actualizar ordenes de Proveedores')),
            ('editar_ordenes_proveedor', ('Editar ordenes de Proveedores')),

        }

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SolicitudPedido, self).save()

   

class ProductosSolicitud(ClaseModelo):
    id_detalle = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, blank=True)
    solicitud = models.ForeignKey(SolicitudPedido, on_delete=models.CASCADE, blank =True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return 'registro de producto {} en la solicitud {}'.format(self.producto, self.solicitud )
    

    class Meta:
        permissions = {
            ('crear_producto_pedido', ('Agregar Producto a Pedido')),
            ('editar_producto_pedido', ('Editar Producto a Pedido')),
#            ('actualizar_unidad_meidida', ('Actualizar Unidad Medida')),
        }


#modelo para el registro de ingreso a bodega y asi actualizar el stock
class TipoOrdenBodega(ClaseModelo):
    id_tipo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.descripcion)

class OrdenBodega(ClaseModelo):
    id_orden = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(SolicitudPedido, on_delete=models.CASCADE, blank=True, null=True, related_name='solicitud_bodega')
    orden_produccion = models.IntegerField(blank=True, null=True, default=None)
    encargado = models.ForeignKey(Usuarios, on_delete=models.CASCADE, blank=True, null=True)
    # campo que define si es un ingreso o una salida de bodega
    tipo = models.ForeignKey(TipoOrdenBodega, on_delete=models.CASCADE, blank=True)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{}-{}'.format(self.id_orden, self.tipo)

    class Meta:
        permissions = {
            ('crear_orden_ingreso', ('Agregar Orden de Ingreso')),
            ('ver_orden_ingreso', ('Ver Orden de Ingreso a Bodega')),
            ('ver_orden_salida', ('Ver Ordenes de Salida de Bodega')),
           ('actualizar_orden_ingreso', ('Actualizar Orden de Ingreso')),
        }


class DetalleOrdenBodega(ClaseModelo):
    id_detalle = models.AutoField(primary_key=True)
    orden = models.ForeignKey(OrdenBodega, on_delete=models.CASCADE, blank=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return '{}-{}'.format(self.producto, self.cantidad)



#modelo de solicitu de produccion
class OrdenProduccion(ClaseModelo):
    id_solicitud = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=500)
    secuencia = models.CharField(max_length=20, blank=True, null=True)
    fecha_almacenado = models.DateTimeField(blank=True, null=True)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, blank=True, null=True )
    total_orden = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)

    #nuevos campos
    usuario_recibe_pedido = models.IntegerField(blank=True, null=True)
    usuario_despacha_pedido = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(OrdenProduccion, self).save()

    class Meta:
        permissions = {
            ('crear_orden_produccion', ('Agregar Orden Produccion')),
            ('editar_orden_produccion', ('Editar Orden Produccion')),
        }

   

class DetalleOrden(ClaseModelo):
    id_detalle = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, blank=True)
    orden = models.ForeignKey(OrdenProduccion, on_delete=models.CASCADE, blank =True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return 'registro de producto {} en la orden {}'.format(self.producto, self.orden )

    class Meta:
        permissions = {
            ('crear_producto_orden', ('Agregar Producto a Orden')),
            ('editar_producto_orden', ('Editar Producto a Orden')),
        }




#agregar signals
def NuevaTransaccion(sender, instance, **kwargs):
    user_obj = Usuarios.objects.filter(pk= instance.usuario_crea).first()
    if instance:
        grupo = 'ws_' + str(user_obj.pais).lower()
    else:
        grupo = 'ws_neutro'
    channel_layer = get_channel_layer()
    print(grupo)
    print(channel_layer)

    async_to_sync(channel_layer.group_send)(
        grupo,
        {
            'type': 'chat_message',
            'message': 'nuevo registro'
        }
    )

post_save.connect(NuevaTransaccion,sender=OrdenBodega)