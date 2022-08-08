from django.http import HttpResponse
import json
import os
from turtle import delay
from wsgiref.util import request_uri

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from trn.serializers import DetalleSolicitudSerializer, SolicitudSerializer
from personal.models import *
from trn.models import *
from prd.models import *

from prd.serializers import *

from datetime import datetime, timedelta, timezone

from trn.tasks import enviarCorreoPrv, notificacion, notificarOrdenProduccion, notificarOrdenProveedor, notificarSolicitudDespachada,\
    notificarBodega

from .forms import *
# Create your views here.
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

from django.conf import settings



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


def crear_pedido(request):
    if request.is_ajax:
        items = request.GET.getlist('itemsSeleccionados[]')
        items = json.loads(items[0])

        infoSolicitud = SolicitudPedido(
            usuario_crea = request.user.id,
            usuario_modifica = request.user.id,
            estado_id = 6
        )
    
        if infoSolicitud:
            infoSolicitud.save()
        
            for producto in items:
                prd_obj = Productos.objects.filter(id_producto=producto).first()
                detalleSolicitud = ProductosSolicitud(
                    usuario_crea = request.user.id,
                    usuario_modifica = request.user.id,
                    producto_id = prd_obj.id_producto,
                    solicitud_id = infoSolicitud.id_solicitud
                )
                if detalleSolicitud:
                    detalleSolicitud.save()
            
            return JsonResponse({'id_solicitud': infoSolicitud.id_solicitud})


@csrf_exempt
def detalle_solicitud(request, id_solicitud=None):
    #culminar orden y enviar a proveedor
    template_name = 'trn/solicitud_pedido_form.html'
    template_reporte = 'trn/comprobante_pedido.html'
    path = settings.MEDIA_ROOT + "\\reportes\\reporte_orden_proveedor.pdf"
    contexto = {}
    form_class = SolicitudForm
    solicitud = SolicitudPedido.objects.filter(id_solicitud=id_solicitud).first()
    if request.method == 'GET':
        if solicitud:
            form_class = SolicitudForm(instance=solicitud)
            detalles_pedidos = ProductosSolicitud.objects.filter(solicitud_id=solicitud.id_solicitud)

        contexto = {
            'form': form_class,
            'solicitud': solicitud,
            'detalles': detalles_pedidos
        }
    else:
        descripcion = request.POST['descripcion']
        proveedor_id = request.POST['proveedor']
        insumos = request.POST.getlist('insumos[]')
        insumos = json.loads(insumos[0])

        if not proveedor_id:
            return JsonResponse({'mensaje': 'Seleccione un proveedor'}, status=500)
        if not descripcion:
            return JsonResponse({'mensaje': 'Ingrese un detalle del pedido'}, status=500)
        
        
        if solicitud:
            solicitud.descripcion = descripcion
            solicitud.proveedor_id = proveedor_id
            solicitud.estado_id = 8
            solicitud.save()

            for insumo in insumos:
                detalle = ProductosSolicitud.objects.\
                    filter(
                        producto_id=insumo.get('id_insumo'),
                        solicitud_id=solicitud.id_solicitud
                    ).first()
                insumo_obj = Productos.objects.filter(id_producto=insumo.get('id_insumo')).first()
                if insumo_obj.estado.descripcion == 'NO DISPONIBLE':
                    if insumo.get('cantidad') != '':
                        if float(insumo_obj.cantidad_minima) > float(insumo.get('cantidad')):
                            return JsonResponse({'mensaje': 'Cantidad es menor a la minima.'}, status=500)
                    else:
                        return JsonResponse({'mensaje': 'Ingrese una cantidad'}, status=500)
                detalle.cantidad = insumo.get('cantidad')
                detalle.save()

                #actualizar el estado del producto a solicitado
                producto_obj = Productos.objects.filter(id_producto=insumo.get('id_insumo')).first()
                producto_obj.estado_id = 12
                producto_obj.save()

            correo_proveedor = solicitud.proveedor.correo
            detalles = ProductosSolicitud.objects.filter(solicitud_id=solicitud.id_solicitud)
            total_pedido = 0
            for d in detalles:
                total_pedido += float(d.cantidad)
                
            solicitud.fecha_envio = datetime.now()
            solicitud.estado_id = 8
            solicitud.total_envio = total_pedido
            solicitud.save()
            
            contexto = {
                'pedido': solicitud,
                'sUrl' : settings.BASE_DIR,
                'detalles': detalles,
                'total_pedido': total_pedido
            }

            archivo = open(path, 'w+b')
            template = get_template(template_reporte)
            html = template.render(contexto)

            pisaStatus = pisa.CreatePDF(
                html,
                dest=archivo
            )
            archivo.close()
            if pisaStatus.err:
                return pisaStatus.err

            correo = [str(correo_proveedor)]
            enviarCorreoPrv.delay(solicitud.id_solicitud, correo)
            notificarOrdenProveedor.delay(proveedor_id, request.user.id, solicitud.id_solicitud)

#            enviarCorreoPrv.delay(solicitud.id_solicitud,correo)

    return render(request, template_name, contexto)

#@login_required(login_url='/login/')
def pedidos_list(request):
    template_name = 'trn/pedidos_list.html'
    contexto = {}

    return render(request, template_name, contexto)



# @login_required(login_url='/login/')
def solicitud_modal(request, id_solicitud=None):
    template_name = 'trn/solicitud_modal.html'
    contexto={}
    solicitud = SolicitudPedido.objects.filter(id_solicitud=id_solicitud).first()
    orden_bodega = OrdenBodega.objects.filter(pedido_id=solicitud.id_solicitud).first()
    orden_relacionada = False
    if orden_bodega:
        orden_relacionada = True
    if request.method == 'GET':
        contexto = {
            'solicitud': solicitud,
            'detalles': ProductosSolicitud.objects.filter(solicitud_id=id_solicitud),
            'orden_bodega': orden_relacionada
        }
   
    return render(request, template_name, contexto)


def generar_orden(request, id_solicitud=None):
    # generar orden hacia bodega
    if request.is_ajax and request.method == 'GET':
        if id_solicitud:
            solicitud = SolicitudPedido.objects.filter(id_solicitud=id_solicitud).first()
            solicitud.estado_id = 9
            solicitud.save()
            detalle_solicitud = ProductosSolicitud.objects.filter(solicitud_id=id_solicitud)
            encargado = Usuarios.objects.filter(rol__descripcion='BODEGUERO').first()
            tipo_orden = TipoOrdenBodega.objects.filter(descripcion='ENTRADA').first()
            infoIngreso = OrdenBodega(
                usuario_crea = request.user.id,
                usuario_modifica=  request.user.id,
                encargado_id = encargado.id,
                pedido_id = solicitud.id_solicitud,
                tipo = tipo_orden,
                estado_id = 3
            )
            if infoIngreso:
                infoIngreso.save()

            for detalle in detalle_solicitud:
                infoDetalle = DetalleOrdenBodega(
                    usuario_crea = request.user.id,
                    usuario_modifica = request.user.id,
                    orden_id = infoIngreso.id_orden,
                    producto_id = detalle.producto.id_producto,
                    cantidad = detalle.cantidad
                )
                if infoDetalle:
                    infoDetalle.save()

            return JsonResponse({'mensaje': 'orden registrada'})
        else:
            return JsonResponse({})




def ingresos_list(request):
    template_name = "trn/ordenes_ingreso_list.html"
    if request.user.rol.descripcion == 'ADMINISTRADOR':
        ordenes = OrdenBodega.objects.filter(tipo__descripcion='ENTRADA').order_by('-fecha_creacion')
    else:
        ordenes = OrdenBodega.objects.filter(encargado_id=request.user.id, tipo__descripcion='ENTRADA').order_by('-fecha_creacion')
    contexto = {
        'ordenes': ordenes
    }
    return render(request, template_name, contexto)


def actualiza_stock(request, id_orden=None):
    if request.method == 'GET':
        orden_ingreso = OrdenBodega.objects.filter(id_orden=id_orden).first()
        detalles = DetalleOrdenBodega.objects.filter(orden_id=orden_ingreso.id_orden)
        
        for detalle in detalles:
            prod = Productos.objects.filter(id_producto=detalle.producto_id).first()
            prod.cantidad_existente = float(prod.cantidad_existente) + float(detalle.cantidad)
            if prod.cantidad_existente >= 1:
                prod.estado_id = 10
            prod.save()
        orden_ingreso.estado_id = 5
        orden_ingreso.save()
        return JsonResponse({'mensaje': 'stock actualizado'})


def informacion_pedido(request, id_solicitud=None):
    if request.method == 'GET':
        if id_solicitud:
            pedido = SolicitudPedido(id_solicitud=id_solicitud).first()
            if pedido:
                print(pedido)


def  listado_pedidos_ajax(request):
    if request.method == 'GET':
        estados = request.GET['estadosBusqueda[]']
        estados = json.loads(estados)
        datos = (json.loads(json.dumps(request.GET)))
        proveedor = request.GET['proveedor_id']
        if proveedor != None:
            proveedor = request.GET['proveedor_id']
        body = {
            'estados': estados,
            'proveedor_id': proveedor,
            'opcion': datos['opcion'],
            'fechaInicio': datos['f_inicio'],
            'fechaFin': datos['f_fin'],
        }
        
        pedidos = obtenerPedidos(body)
        serializer = SolicitudSerializer(pedidos, many=True).data
        return JsonResponse({'pedidos': serializer, 'registros': pedidos.count()})



def obtenerPedidos(filtros):
    estados = filtros.get('estados')
    proveedor_id = filtros.get('proveedor_id')
    f_inicio = filtros.get('fechaInicio')
    f_fin = filtros.get('fechaFin')
    opcion = filtros.get('opcion')
    ahora = datetime.now()
    dia_uno_mes_actual = ahora.replace(
        day=1,
        hour=0,
        minute=0,
        second=0
    )
    dia_uno_mes_anterior = dia_uno_mes_actual - timedelta(days=1)
    dia_uno_mes_anterior = dia_uno_mes_anterior.replace(
        day=1,
        hour=0,
        minute=0,
        second=0
    )
    f_inicio = datetime.strptime(f_inicio, '%Y-%m-%d').date()
    f_fin = datetime.strptime(f_fin, '%Y-%m-%d').date()

    if opcion == '1':
        f_inicio = dia_uno_mes_actual
        f_fin = ahora  + timedelta(days=1)
    if opcion == '2':
        f_inicio = dia_uno_mes_anterior
        f_fin = dia_uno_mes_actual
    if opcion == '3':
        f_inicio = f_inicio
        f_fin = f_fin + timedelta(days=1)

    estados_id = {}
    
    if len(estados):
        estados_id = Estados.objects.\
            filter(
                id_estado__in = estados
            ).values('id_estado')
    if len(estados_id) >= 1:
        if proveedor_id != '0':
            pedidos = SolicitudPedido.objects.\
                filter(
                    estado_id__in=estados_id,
                    proveedor_id=proveedor_id,
                    fecha_creacion__gte=f_inicio,
                    fecha_creacion__lte=f_fin
                ).order_by('-fecha_creacion')
        else:
            pedidos = SolicitudPedido.objects.\
                filter(
                    estado_id__in=estados_id,
                    fecha_creacion__gte=f_inicio,
                    fecha_creacion__lte=f_fin
                ).order_by('-fecha_creacion')
        
    else:
        if proveedor_id != '0':
            pedidos = SolicitudPedido.objects.\
                filter(
                    proveedor_id=proveedor_id,
                    fecha_creacion__gte=f_inicio,
                    fecha_creacion__lte=f_fin
                ).order_by('-fecha_creacion')
        else:
            pedidos = SolicitudPedido.objects.\
                filter(
                    fecha_creacion__gte=f_inicio,
                    fecha_creacion__lte=f_fin
                ).order_by('-fecha_creacion')
    return pedidos


def enviar_orden(request, id_solicitud=None):
    if request.method == 'GET':
        template_name = 'trn/comprobante_pedido.html'
        contexto = {}
        path = settings.MEDIA_ROOT + "\\reportes\\reporte_orden_proveedor.pdf"

        if id_solicitud:
            pedido_obj = SolicitudPedido.objects.filter(id_solicitud=id_solicitud).first()
            detalles = ProductosSolicitud.objects.filter(solicitud_id=pedido_obj.id_solicitud)
            total_pedido = 0
            for d in detalles:
                total_pedido += float(d.cantidad)
                
            pedido_obj.fecha_envio = datetime.now()
            pedido_obj.estado_id = 8
            pedido_obj.total_envio = total_pedido
            pedido_obj.save()
            
            contexto = {
                'pedido': pedido_obj,
                'sUrl' : settings.BASE_DIR,
                'detalles': detalles,
                'total_pedido': total_pedido
            }  
            
            correo_proveedor = pedido_obj.proveedor.correo
            correo = [str(correo_proveedor)]

            #ejemplo  pdf en response
            # response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'inline; filename="reporte.pdf"'
            # # response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
            # template = get_template(template_name)
            # html = template.render(contexto)

            # # create a pdf
            # pisaStatus = pisa.CreatePDF(
            #     html, dest=response, link_callback=link_callback)
            # # if error then show some funy view
            # if pisaStatus.err:
            #     return HttpResponse('We had some errors <pre>' + html + '</pre>')


            archivo = open(path, 'w+b')
            template = get_template(template_name)
            html = template.render(contexto)

            pisaStatus = pisa.CreatePDF(
                html,
                dest=archivo
            )
            archivo.close()
            if pisaStatus.err:
                return pisaStatus.err

            # tarea para el envio de correo al proveedor con la orden generada
            enviarCorreoPrv.delay(id_solicitud,correo)
            return JsonResponse({'mensaje': 'correcto'}, status=200)
            # return response

        else:
            return JsonResponse({'mensaje': 'No se encontro pedido con le id.'}, status=500)


def recibir_pedido(request, id_solicitud=None):
    if request.method == 'GET':
        pedido_obj = SolicitudPedido.objects.filter(id_solicitud=id_solicitud).first()
        pedido_obj.estado = Estados.objects.filter(descripcion='REVISION PROVEEDOR SOLICITUD').first()
        pedido_obj.fecha_recibida = datetime.now()
        pedido_obj.save()


        return JsonResponse({'mensaje': 'orden registrada'})


def marcar_orden_revisada(request, id_orden=None):
    if request.method == 'GET':
        orden_obj = OrdenBodega.objects.filter(id_orden=id_orden).first()
        orden_obj.estado = Estados.objects.filter(descripcion='ORDEN REVISADA BODEGA').first()
        orden_obj.save()

        return JsonResponse({'mensaje': 'orden revisada'})


def revisar_orden_produccion(request, id_orden=None):
    if request.method == 'GET':
        orden_obj = OrdenProduccion.objects.filter(id_solicitud=id_orden).first()
        # query consulta de producto de la orden si existen proudctos en bodega.
        productos_id = DetalleOrden.objects.filter(orden_id=orden_obj.id_solicitud)
        for p in productos_id:
            prd_obj = Productos.objects.filter(id_producto=p.producto_id).first()
            if prd_obj.cantidad_existente < p.cantidad:
                return JsonResponse({'mensaje': 'No exiten suficientes insumos para abastecer solicitud.'}, status=500)



        orden_obj.estado = Estados.objects.filter(descripcion='SOLICITUD DE PROD. REVISADA').first()
        orden_obj.save()

        return JsonResponse({'mensaje': 'orden revisada'})




def despachar_pedido(request, id_solicitud=None):
    if request.method == 'GET':
        pedido_obj = SolicitudPedido.objects.filter(id_solicitud=id_solicitud).first()
        pedido_obj.estado = Estados.objects.filter(descripcion='SOLICITUD DE PEDIDO DESPACHADA').first()
        pedido_obj.fecha_recibida = datetime.now()
        pedido_obj.save()
        
        #generar notificacion
        notificarSolicitudDespachada.delay(pedido_obj.id_solicitud, request.user.id, pedido_obj.usuario_crea)
        

        return JsonResponse({'mensaje': 'orden registrada'})



def generar_orden_ingreso(request, id_solicitud=None):
    if request.method == 'GET':
        id_solicitud = request.GET['solicitud']
        encargado_id = request.GET['usuario_encargado']
        if id_solicitud:
            solicitud_obj = SolicitudPedido.objects.filter(id_solicitud=id_solicitud).first()
            detalle_solicitud = ProductosSolicitud.objects.filter(solicitud_id=solicitud_obj.id_solicitud)
            encargado = Usuarios.objects.filter(id=encargado_id).first()
            tipo_orden = TipoOrdenBodega.objects.filter(descripcion='ENTRADA').first()
            infoIngreso = OrdenBodega(
                usuario_crea = request.user.id,
                usuario_modifica=  request.user.id,
                encargado_id = encargado.id,
                pedido_id = solicitud_obj.id_solicitud,
                tipo = tipo_orden,
                estado_id = 3
            )
            if infoIngreso:
                infoIngreso.save()

            for detalle in detalle_solicitud:
                infoDetalle = DetalleOrdenBodega(
                    usuario_crea = request.user.id,
                    usuario_modifica = request.user.id,
                    orden_id = infoIngreso.id_orden,
                    producto_id = detalle.producto.id_producto,
                    cantidad = detalle.cantidad
                )
                if infoDetalle:
                    infoDetalle.save()
                

            notificarBodega.delay(infoIngreso.id_orden, request.user.id, encargado_id)

        
        

        return JsonResponse({'mensaje': 'orden registrada'})






def generar_documento(request, id_solicitud=None):
    template_name = 'trn/comprobante_pedido.html'
    contexto = {}
    path = settings.MEDIA_ROOT + "\\reportes\\reporte_orden_proveedor.pdf"
    if id_solicitud:
        pedido_obj = SolicitudPedido.objects.filter(id_solicitud=id_solicitud).first()
        detalles = ProductosSolicitud.objects.filter(solicitud_id=pedido_obj.id_solicitud)
        total_pedido = 0
        for d in detalles:
            total_pedido += float(d.cantidad)
            
        contexto = {
            'pedido': pedido_obj,
            'sUrl' : settings.BASE_DIR,
            'detalles': detalles,
            'total_pedido': total_pedido
        }
        
                    
        
        correo_proveedor = pedido_obj.proveedor.correo
        correo = [str(correo_proveedor)]

        #ejemplo  pdf en response
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte_pedido.pdf"'
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



#mostrar listado de ordenes de produccion
def orden_produccion_list(request):
    template_name = 'trn/orden_produccion_list.html'
    contexto = {
        'ordenes': OrdenProduccion.objects.all().order_by('-id_solicitud')
    }
    return render(request, template_name, contexto)



def orden_produccion_modal(request, id_orden=None):
    template_name = 'trn/orden_produccion_modal.html'
    contexto={}
    orden_obj = OrdenProduccion.objects.filter(id_solicitud=id_orden).first()
    if request.method == 'GET':
        if orden_obj:
            encargado_recibir_insumos = ''
            print(orden_obj.usuario_recibe_pedido)
            if orden_obj.usuario_recibe_pedido != None:
                empleado = PersonalFinca.objects.filter(id_personal=orden_obj.usuario_recibe_pedido).first()
                encargado_recibir_insumos = empleado.nombres + ' ' +empleado.apellidos
            contexto = {
                'orden': orden_obj,
                'detalles': DetalleOrden.objects.filter(orden_id=orden_obj.id_solicitud),
                'encargado': encargado_recibir_insumos
            }
        else:
            form = OrdenProduccionForm()
            contexto = {
                'form': form
            }
        
    return render(request, template_name, contexto)


from prd.serializers import ProductosSerializer

def lista_productos_ajax(request):
    if request.method == 'GET':
        categoria_id = request.GET['categoria_id']
        if categoria_id:

        #obtener los productos para mostrar en el listado de orden de pruccion
            productos = Productos.objects.filter(categoria_id=categoria_id)
            serializer = ProductosSerializer(productos, many=True).data

        return JsonResponse({'data': serializer})


def orden_produccion_crear(request):
    if request.is_ajax:
        items = request.GET.getlist('itemsSeleccionados[]')
        items = json.loads(items[0])

        ultima_orden = OrdenProduccion.objects.all().last()
        if ultima_orden:
            secuencia = 'ORD-00'+str(int(ultima_orden.id_solicitud)+1)
        else:
            secuencia = 'ORD-00'+str(1)

        infoOrden = OrdenProduccion(
            usuario_crea = request.user.id,
            usuario_modifica = request.user.id,
            secuencia = secuencia,
            estado_id = 3
        )
        if infoOrden:
            infoOrden.save()

            for producto in items:
                prd_obj = Productos.objects.filter(id_producto=producto).first()
                detalleOrden = DetalleOrden(
                    usuario_crea = request.user.id,
                    usuario_modifica = request.user.id,
                    producto_id = prd_obj.id_producto,
                    orden_id = infoOrden.id_solicitud
                )
                if detalleOrden:
                    detalleOrden.save()

        return JsonResponse({'id_orden': infoOrden.id_solicitud})


@csrf_exempt
def detalle_orden_produccion(request, id_orden=None):
    #culminar orden y enviar a proveedor
    template_name = 'trn/orden_produccion_form.html'
    template_reporte = 'trn/comprobante_pedido.html'
    path = settings.MEDIA_ROOT + "\\reportes\\reporte_orden_roduccion.pdf"
    contexto = {}
    form_class = OrdenProduccionForm

    orden = OrdenProduccion.objects.filter(id_solicitud=id_orden).first()
    if request.method == 'GET':
        empleados = PersonalFinca.objects.all()
        if orden:
            
            form_class = OrdenProduccionForm(instance=orden)
            detalles_orden = DetalleOrden.objects.filter(orden_id=orden.id_solicitud)

        contexto = {
            'form': form_class,
            'orden': orden,
            'detalles': detalles_orden,
            'empleados': empleados,
        }
    else:
        descripcion = request.POST['descripcion']
        insumos = request.POST.getlist('insumos[]')
        insumos = json.loads(insumos[0])
        personal_id = request.POST['personal_id']
        if descripcion == '':
            return JsonResponse({'mensaje': ('ingrese la descripcion')}, status=500)
        if orden:
            orden.descripcion = descripcion
            
            orden.usuario_recibe_pedido = personal_id
            orden.save()
            print(orden)
            total_orden = 0
            for insumo in insumos:
                print(insumo)
                insumo_obj = Productos.objects.filter(id_producto=insumo.get('id_insumo')).first()
                if insumo.get('cantidad') == '':
                    return JsonResponse({'mensaje': ('ingrese la cantidad para el insumo {}').format(insumo_obj.descripcion)}, status=500)
                else:
                    if float(insumo_obj.cantidad_existente) < float(insumo.get('cantidad')):
                        return JsonResponse({'mensaje': ('cantidad es mayor a la existente, cantidad disponible {}, insumo: {}').format(insumo_obj.cantidad_existente, insumo_obj.descripcion)}, status=500)
                detalle = DetalleOrden.objects.\
                    filter(
                        producto_id=insumo.get('id_insumo'),
                        orden_id=orden.id_solicitud
                    ).first()
                detalle.cantidad = insumo.get('cantidad')
                detalle.save()
                total_orden = total_orden + int(insumo.get('cantidad'))
            orden.estado_id = 13
            orden.total_orden = total_orden
            orden.save()

            #     contexto = {
            #         'pedido': solicitud,
            #         'sUrl' : settings.BASE_DIR,
            #         'detalles': detalles,
            #         'total_pedido': total_pedido
            #     }

            #     archivo = open(path, 'w+b')
            #     template = get_template(template_reporte)
            #     html = template.render(contexto)

            #     pisaStatus = pisa.CreatePDF(
            #         html,
            #         dest=archivo
            #     )
            #     archivo.close()
            #     if pisaStatus.err:
            #         return pisaStatus.err

            #     correo = [str(correo_proveedor)]
            
            encargado_obj = Usuarios.objects.filter(rol__descripcion='BODEGUERO').first()
            notificarOrdenProduccion.delay(encargado_obj.id, request.user.id, orden.id_solicitud) 

    return render(request, template_name, contexto)


def ordenes_salida_list(request):
    template_name = 'trn/ordenes_salida_list.html'
    contexto = {
        'ordenes': OrdenBodega.objects.filter(tipo__descripcion='SALIDA').order_by('-fecha_creacion')
    }
    return render(request, template_name, contexto)


def procesar_orden(request, id_orden=None):
    estado_peticion = False
    if request.method == 'GET':
        orden_obj = OrdenProduccion.objects.filter(id_solicitud=id_orden).first()
        if orden_obj:
            detalles = DetalleOrden.objects.filter(orden_id=orden_obj.id_solicitud)
            lista_falatante = []
            for detalle in detalles:
                producto = Productos.objects.filter(id_producto=detalle.producto_id).first()
                print('prod')
                print(producto.cantidad_existente)
                if int(detalle.cantidad) > producto.cantidad_existente:
                    lista_falatante.append(producto)
            if len(lista_falatante) >= 1:
                estado_peticion = False
                return JsonResponse({'estado': estado_peticion})
            else:
                return JsonResponse({'estado': True})
                

def generar_orden_salida(request, id_orden=None):
    #obtener orden de produccion consultar detalles y generar la orden de salida
    if id_orden:
        orden_obj = OrdenProduccion.objects.filter(id_solicitud=id_orden).first()
        orden_obj.estado_id = 14
        orden_obj.save()
        detalles = DetalleOrden.objects.filter(orden_id=orden_obj.id_solicitud)

        encargado = Usuarios.objects.filter(rol__descripcion='BODEGUERO').first()
        infoOrdenBodega = OrdenBodega(
            usuario_crea = request.user.id,
            usuario_modifica = request.user.id,
            estado_id = 3,
            encargado_id = encargado.id,
            orden_produccion = orden_obj.id_solicitud,
            tipo_id = 2
        )
        if infoOrdenBodega:
            infoOrdenBodega.save()

            for detalle in detalles:
                detalle_orden = DetalleOrdenBodega(
                    usuario_crea=request.user.id,
                    usuario_modifica=request.user.id,
                    cantidad = detalle.cantidad,
                    orden_id = infoOrdenBodega.id_orden,
                    producto_id = detalle.producto.id_producto
                )
                if detalle_orden:
                    detalle_orden.save()

        return HttpResponseRedirect('/')

def generar_orden_salida_bodega(request):
    #obtener orden de produccion consultar detalles y generar la orden de salida
    if request.GET['usuario_encargado']:
        encargado_obj = Usuarios.objects.filter(id=request.GET['usuario_encargado']).first()
    orden_obj = OrdenProduccion.objects.filter(id_solicitud=request.GET['solicitud']).first()
    orden_obj.estado_id = 14
    orden_obj.save()
    detalles = DetalleOrden.objects.filter(orden_id=orden_obj.id_solicitud)

    infoOrdenBodega = OrdenBodega(
        usuario_crea = request.user.id,
        usuario_modifica = request.user.id,
        estado_id = 3,
        encargado_id = encargado_obj.id,
        orden_produccion = orden_obj.id_solicitud,
        tipo_id = 2
    )
    if infoOrdenBodega:
        infoOrdenBodega.save()

        for detalle in detalles:
            detalle_orden = DetalleOrdenBodega(
                usuario_crea=request.user.id,
                usuario_modifica=request.user.id,
                cantidad = detalle.cantidad,
                orden_id = infoOrdenBodega.id_orden,
                producto_id = detalle.producto.id_producto
            )
            if detalle_orden:
                detalle_orden.save()

        notificarBodega.delay(infoOrdenBodega.id_orden, request.user.id, encargado_obj.id)

    return HttpResponseRedirect('/')

    

def actualiza_stock_salida(request, id_orden=None):
    if request.method == 'GET':
        orden_salida = OrdenBodega.objects.filter(id_orden=id_orden).first()
        
        detalles = DetalleOrdenBodega.objects.filter(orden_id=orden_salida.id_orden)
        for detalle in detalles:
            prod = Productos.objects.filter(id_producto=detalle.producto_id).first()
            resultado = float(prod.cantidad_existente) - float(detalle.cantidad)
            if resultado < 0:
                return JsonResponse({'mensaje': 'No existe suficientes insumos para la solicitud.'}, status=500)
            if resultado == 0:
                prod.estado_id = 11
            if resultado > 0 and resultado < prod.cantidad_minima:
                prod.estado_id = 22
            if resultado >= prod.cantidad_minima:
                prod.estado_id = 10
            prod.cantidad_existente = resultado
            prod.save()
        orden_salida.estado_id = Estados.objects.filter(descripcion='ORDEN BODEGA PROCESADA').first()
        orden_salida.save()
        if orden_salida.orden_produccion:
            orden_prd = OrdenProduccion.objects.filter(id_solicitud=orden_salida.orden_produccion).first()
            orden_prd.estado = Estados.objects.filter(descripcion='SOLICITUD DE PROD. FINALIZADA').first()
            orden_prd.save()
        return JsonResponse({'mensaje': 'stock actualizado'})



def orden_ingreso_detalle(request, id_orden=None):
    template_name = 'trn/orden_ingreso_modal.html'
    orden_obj = OrdenBodega.objects.filter(id_orden=id_orden).first()
    contexto = {
        'orden': OrdenBodega.objects.filter(id_orden=id_orden).first(),
        'detalles': DetalleOrdenBodega.objects.filter(orden_id=orden_obj.id_orden)

    }

    return render(request, template_name, contexto)



def orden_salida_detalle(request, id_orden=None):
    template_name = 'trn/orden_salida_modal.html'
    orden_obj = OrdenBodega.objects.filter(id_orden=id_orden).first()
    contexto = {
        'orden': OrdenBodega.objects.filter(id_orden=id_orden).first(),
        'detalles': DetalleOrdenBodega.objects.filter(orden_id=orden_obj.id_orden)

    }

    return render(request, template_name, contexto)


def lista_categorias_productos(request):
    if request.is_ajax:
        categorias = CategoriaProducto.objects.filter(estado__descripcion__iexact='ACTIVO')
        # serializer
        serializer = CategoriaProductoSerializers(categorias, many=True).data

        return JsonResponse({'data': serializer})




def eliminar_insumo_solic_produccion(request):
    if request.is_ajax:
        id_insumo = request.GET['id_insumo']
        id_orden = request.GET['id_orden']
        if id_insumo:
            detalle_orden = DetalleOrden.objects.filter(orden_id=id_orden, producto_id=id_insumo).first()
            detalle_orden.delete()
            estado = 1
        else:
            estado = 2
        data = {
            'estado': estado
        }
        return JsonResponse({'data': data})


def eliminar_solicitud_prod(request):
    if request.is_ajax:
        id_orden = request.GET['id_solicitud']
        if id_orden:
            orden_obj = OrdenProduccion.objects.filter(id_solicitud=id_orden).first()
            orden_obj.delete()
            estado = 1
        else:
            estado = 2
        data = {
            'estado': estado
        }
        return JsonResponse({'data': data})