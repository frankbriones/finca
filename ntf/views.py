from django.shortcuts import render

from ntf.serilizers import NotificacionSerializer
from django.http import JsonResponse

from .models import *
# Create your views here.
def obtener_notificacion(request):
    if request.method == 'GET':
        user_id = request.GET['usuario_id']
        user_obj = Usuarios.objects.filter(id=user_id).first()
        if not user_obj:
            notificaciones = Notificacion.objects.filter(proveedor_id=user_id, vista=False).first()
        else:
            notificaciones = Notificacion.objects.filter(encargado_id=user_id, vista=False).first()
        
        serializer = NotificacionSerializer(notificaciones, many=False).data
        return JsonResponse({
            'data': serializer
        })


def actualizar_notificacion(request):
    if request.method == 'GET':
        id_notificacion = request.GET['idNotificacion']
        if Notificacion.objects.filter(id_notificacion=id_notificacion).exists():
            ntf_obj = Notificacion.objects.filter(id_notificacion=id_notificacion).first()
            if ntf_obj:
                ntf_obj.vista = True
                ntf_obj.save()
            return JsonResponse({'mensaje': 'notificacion actualizada'})
        