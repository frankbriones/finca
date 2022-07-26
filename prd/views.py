from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect

from prd.resources import ProductoResource

from .models import *
from prd.forms import ProductoForm

# Create your views here.
def productos_list(request):
    mensaje = None
    if 'mensaje' in request.session:
        mensaje = request.session['mensaje']
        del request.session['mensaje']


    template_name = 'prd/productos_list.html'
    productos = Productos.objects.all()
    contexto = {
        'productos': productos,
        'mensaje': mensaje
    }
    return render(request, template_name, contexto)


def detalle_producto(request, id_producto=None):
    template_name = 'prd/editar_producto.html'
    contexto = {}
    form_class = ProductoForm
    producto = Productos.objects.filter(id_producto=id_producto).first()
    mensaje = ""
    if request.method == 'GET':
        
        form_class = ProductoForm(instance=producto)
        contexto = {
            'form': form_class,
            'producto': producto
        }
    else:
        # form_class = ProductoForm(request.POST)
        # if form_class.is_valid():
        #     producto = form_class.save(commit=False)
        #     producto.usuario_crea = request.user.id
        #     producto.usuario_modifica = request.user.id
        #     producto.estado_id = 4
        #     producto.save()
        #     if producto.cantidad_existente >= producto.cantidad_minima:
        #         producto.estado_id = 4
        #         producto.save()

        #     request.session['mensaje'] = "Nuevo insumo registrado"

        #     return HttpResponseRedirect('/products/productos_list/')

        # UNA MANERA DIFRENTE DE ALMACENAR DATOS
        
        descripcion = request.POST['descripcion']
        categoria = request.POST['categoria']
        unidad_medida = request.POST['unidad_medida']
        cantidad_minima = request.POST['cantidad_minima']
        bodega = request.POST['bodega']
        seccion = request.POST['seccion']
        if id_producto:
            producto.descripcion = descripcion
            producto.categoria_id = categoria
            producto.unidad_medida_id = unidad_medida
            producto.cantidad_minima = cantidad_minima
            producto.bodega_id = bodega
            producto.seccion_id = seccion
            producto.save()
            if float(producto.cantidad_minima) > float(producto.cantidad_existente):
                if producto.estado_id != 12:
                    producto.estado_id = 11
            producto.save()
            request.session['mensaje'] = "Edicion de Insumo {}".format(descripcion)
        else:
            
            # infProducto = Productos(
            #     descripcion = descripcion,
            #     categoria_id = categoria,
            #     unidad_medida_id = unidad_medida,
            #     cantidad_minima = cantidad_minima,
            #     seccion_id = seccion,
            #     usuario_crea=request.user.id,
            #     usuario_modifica = request.user.id,
            #     estado_id=1
            # )
            # if infProducto:
            #     infProducto.save()

            form_class = ProductoForm(request.POST)
            if form_class.is_valid():
                producto = form_class.save(commit=False)
                producto.usuario_crea = request.user.id
                producto.usuario_modifica = request.user.id
                producto.estado_id = 11
                producto.save()
                if producto.cantidad_existente >= producto.cantidad_minima:
                    producto.estado_id = 10
                    producto.save()


                request.session['mensaje'] = "Nuevo insumo registrado"
                return HttpResponseRedirect('/products/productos_list/')
            contexto = {
                'form': form_class
            }
            return render(request, template_name, contexto)
        return HttpResponseRedirect('/products/productos_list/')
    return render(request, template_name, contexto)



from rest_framework.views import APIView
from datetime import datetime, timezone
from django.http.response import HttpResponseRedirect, JsonResponse, HttpResponse


class StockReporte(APIView):
    def post(self, request):
        filtros = self.request
        productos = BusquedaProductos(
            filtros
        )
        productos_lista = []
        if productos:
            ahora = datetime.now(timezone.utc)
            for producto in productos:
                productos_lista.append(producto)
            producto_resource = ProductoResource()
            dataset = producto_resource.export(productos_lista)
            nombre_archivo = 'Reporte_Stock_' + \
                ahora.strftime('%d-%m-%Y') + '.xls'
            response = HttpResponse(
                dataset.xls,
                content_type='application/vnd.ms-excel'
            )
            response['Content-Disposition'] = 'attachment; filename=' \
                + nombre_archivo
        else:
            response = HttpResponse('No existen ordenes')
        return response


def BusquedaProductos(filtros):
    fecha_inicial = filtros.POST['query']
    fecha_final = filtros.POST['query2']

    productos = Productos.objects.filter(
        fecha_creacion__gte=fecha_inicial,
        fecha_creacion__lte=fecha_final
    ).order_by('-fecha_creacion')
    return productos