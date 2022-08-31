from datetime import datetime, timedelta 
import json
import os

from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from django.conf import settings
from django.template.loader import get_template


from prd.models import *
from trn.models import DetalleOrden, OrdenProduccion, ProductosSolicitud, SolicitudPedido




from xhtml2pdf import pisa


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL
    sRoot = settings.STATIC_ROOT
    mUrl = settings.MEDIA_URL
    mRoot = settings.MEDIA_ROOT

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path






# Create your views here.
@login_required(login_url='/login/')
def stock_bodega(request):
    template_name = 'inv/stock_list.html'
    lista_estados = ['12', '10']
    for p in Productos.objects.all().exclude(estado_id__in=lista_estados):
        if p.cantidad_existente <= p.cantidad_minima and p.cantidad_existente != 0:
            estado = 22
        else:
            if p.cantidad_existente == 0:
                estado = 11
            else:   
                estado = 10
        p.estado_id = estado
        p.save()
    productos = Productos.objects.all()

    contexto = {
        'inventario': productos
    }
    return render(request, template_name, contexto)




def InventarioReporte(request):
    template_name = 'inv/reporte_stock.html'
    contexto = {}
    inventario = {
        'codigo': '',
        'descripcion': '',
        'fecha_movimiento': '',
        'cantidad_entreda': 0,
        'cantidad_salida': 0,
        'Cantidad Total': 0
    }
    lista = []
    if request.method == 'POST':
        fecha_inicial =  request.POST['query']
        fecha_final = request.POST['query2']
        solicitudes_prv = SolicitudPedido.objects.filter(
            estado__descripcion__iexact='SOLICITUD DE PEDIDO DESPACHADA',
            fecha_creacion__gte=fecha_inicial,
            fecha_creacion__lte=fecha_final
        ).order_by('-fecha_creacion').values('id_solicitud')

        ordenes_prod = OrdenProduccion.objects.filter(
            estado__descripcion__iexact='ORD PROD. PROCESADA',
            fecha_creacion__gte=fecha_inicial,
            fecha_creacion__lte=fecha_final
        ).order_by('-fecha_creacion').values('id_solicitud')

        if len(solicitudes_prv) <=0 and len(ordenes_prod):
            return JsonResponse({'mensaje': 'error'}, status=500)
        for j in ProductosSolicitud.objects.filter(solicitud_id__in=solicitudes_prv):
            info = {
                'codigo': j.producto.id_producto,
                'descripcion': j.producto.descripcion,
                'fecha_movimiento': j.solicitud.fecha_creacion - timedelta(hours=5),
                'cantidad_entrada': str(j.cantidad),
                'cantidad_salida': 0,
                'cantidad_total': str(j.cantidad)
            }
            lista.append(info)
        for j in DetalleOrden.objects.filter(orden_id__in=ordenes_prod):
            info = {
                'codigo': j.producto.id_producto,
                'descripcion': j.producto.descripcion,
                'fecha_movimiento': (j.orden.fecha_creacion) - timedelta(hours=5),
                'cantidad_entrada': 0,
                'cantidad_salida': str(j.cantidad),
                'cantidad_total': str(j.cantidad)
            }
            lista.append(info)

        contexto = {
            'usuario_genera': request.user.get_full_name(),
            'fecha_creado': datetime.now(),
            'inventario': lista,
            'sUrl' : settings.BASE_DIR,
            'fecha_1': fecha_inicial,
            'fecha_2': fecha_final
        }
        
        # # correo_proveedor = pedido_obj.proveedor.correo
        # # correo = [str(correo_proveedor)]

        # #ejemplo  pdf en response
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte_inventario.pdf"'
        # response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
        template = get_template(template_name)
        html = template.render(contexto)

        # create a pdf
        pisaStatus = pisa.CreatePDF(
            html, dest=response, link_callback=link_callback)
        # if error then show some funy view
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        
        return response