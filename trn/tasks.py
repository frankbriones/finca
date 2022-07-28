from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from datetime import datetime

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import get_template
from ntf.models import Notificacion

from trn.models import *

@shared_task
def enviarCorreoPrv(id_solicitud, correo):
    print('*******************')
    print(correo)
    template_name = 'trn/comprobante_pedido.html'
    contexto = {}
    pedido_obj = SolicitudPedido.objects.filter(id_solicitud=id_solicitud).first()

    contexto = {
        'pedido': pedido_obj,
        'sUrl' : settings.BASE_DIR
    }

    subject = "Solicitud de pedidos de finca xxxx"
    message = "Se Genero el pedido con fecha {}".format(datetime.now())
    from_email = settings.EMAIL_HOST_USER

    path = settings.MEDIA_ROOT + "\\reportes\\reporte_orden_proveedor.pdf"
    to = correo
    contenido = open(path, 'rb').read()
    attachment = ('reporte_pedido.pdf', contenido, 'application/pdf')
    email = EmailMessage(subject, message, bcc=to, from_email=from_email,
                        attachments=[attachment, ])
    print(email)
    email.content_subtype = "text"
    email.send()


@shared_task
def notificacion(id_orden, user_id, encargado_id):
    if OrdenBodega.objects.filter(id_orden=id_orden).exists():
        orden_obj = OrdenBodega.objects.filter(id_orden=id_orden).first()
        infoNotificacion = Notificacion(
            estado_id_id = orden_obj.estado_id,
            orden_id = orden_obj.id_orden,
            encargado_id = orden_obj.encargado_id,
            usuario_crea = user_id,
            vista=False
        )
        if infoNotificacion:
            infoNotificacion.save()
        if orden_obj.pedido.proveedor.pais_id:
            grupo = 'ws_' + str(orden_obj.pedido.proveedor.pais).lower()
        else:
            grupo = 'ws_neutro'
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(grupo,{'type':'chat_message','message': 'nuevo_registro'})


@shared_task
def notificarSolicitudDespachada(id_solicitud, user_id, encargado_id):
    if SolicitudPedido.objects.filter(id_solicitud=id_solicitud).exists():
        orden_obj = SolicitudPedido.objects.filter(id_solicitud=id_solicitud).first()
        infoNotificacion = Notificacion(
            estado_id_id = orden_obj.estado_id,
            orden_prv = orden_obj.id_solicitud,
            encargado_id = orden_obj.usuario_crea,
            usuario_crea = user_id,
            vista=False
        )
        if infoNotificacion:
            infoNotificacion.save()
        if orden_obj.proveedor.pais_id:
            grupo = 'ws_' + str(orden_obj.proveedor.pais).lower()
        else:
            grupo = 'ws_neutro'
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(grupo,{'type':'chat_message','message': 'nuevo_registro'})




@shared_task
def notificarOrdenProduccion(encargado_id, user_id, id_orden):
    if OrdenProduccion.objects.filter(id_solicitud=id_orden).exists():
        orden_obj = OrdenProduccion.objects.filter(id_solicitud=id_orden).first()
        infoNotificacion = Notificacion(
            estado_id_id = orden_obj.estado_id,
            orden_prd = orden_obj.id_solicitud,
            encargado_id = encargado_id,
            usuario_crea = user_id,
            vista=False
        )
        if infoNotificacion:
            infoNotificacion.save()
        usuario = Usuarios.objects.filter(id=user_id).first()
        if usuario.pais_id:
            grupo = 'ws_' + str(usuario.pais).lower()
        else:
            grupo = 'ws_neutro'
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(grupo,{'type':'chat_message','message': 'nuevo_registro'})



@shared_task
def notificarOrdenProveedor(proveedor_id, user_id, solicitud_id):
    print('**')
    if SolicitudPedido.objects.filter(id_solicitud=solicitud_id).exists():
        orden_obj = SolicitudPedido.objects.filter(id_solicitud=solicitud_id).first()
        infoNotificacion = Notificacion(
            estado_id_id = orden_obj.estado_id,
            orden_prv = orden_obj.id_solicitud,
            proveedor_id = proveedor_id,
            usuario_crea = user_id,
            vista=False
        )
        if infoNotificacion:
            infoNotificacion.save()
        usuario = Usuarios.objects.filter(id=user_id).first()
        if usuario.pais_id:
            grupo = 'ws_' + str(usuario.pais).lower()
        else:
            grupo = 'ws_neutro'
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(grupo,{'type':'chat_message','message': 'nuevo_registro'})




@shared_task
def notificarBodega(id_orden, user_id, encargado_id):
    print(id_orden)
    print(user_id)
    print(encargado_id)
    if OrdenBodega.objects.filter(id_orden=id_orden).exists():
        orden_obj = OrdenBodega.objects.filter(id_orden=id_orden).first()
        infoNotificacion = Notificacion(
            estado_id_id = orden_obj.estado_id,
            orden_id = orden_obj.id_orden,
            encargado_id = encargado_id,
            usuario_crea = user_id,
            vista=False
        )
        print('********')
        if infoNotificacion:
            infoNotificacion.save()
        usuario = Usuarios.objects.filter(id=user_id).first()
        if usuario.pais_id:
            grupo = 'ws_' + str(usuario.pais).lower()
        else:
            grupo = 'ws_neutro'
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(grupo,{'type':'chat_message','message': 'nuevo_registro'})



