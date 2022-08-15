import json

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/login/')
def detalle_producto(request, id_producto=None):
    template_name = 'prd/editar_producto.html'
    contexto = {}
    form_class = ProductoForm
    producto = Productos.objects.filter(id_producto=id_producto).first()
    mensaje = ""
    if request.method == 'GET':
        
        form_class = ProductoForm(instance=producto)
        if producto:
            form_class.modificarQuerySet(producto.bodega_id)
        contexto = {
            'form': form_class,
            'producto': producto
        }
    else:
        print(request.POST)
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
            return HttpResponseRedirect('/products/productos_list/')
        else:
            
            infProducto = Productos(
                descripcion = descripcion,
                categoria_id = categoria,
                unidad_medida_id = unidad_medida,
                cantidad_minima = cantidad_minima,
                seccion_id = seccion,
                usuario_crea=request.user.id,
                usuario_modifica = request.user.id,
                estado_id=1
            )
            if infProducto:
                infProducto.save()

            # form_class = ProductoForm(request.POST)
            # if form_class.is_valid():
            #     print('asdasdad')
            #     producto = form_class.save(commit=False)
            #     producto.usuario_crea = request.user.id
            #     producto.usuario_modifica = request.user.id
            #     producto.estado_id = 11
            #     producto.save()
            #     if producto.cantidad_existente >= producto.cantidad_minima:
            #         producto.estado_id = 10
            #         producto.save()


                request.session['mensaje'] = "Nuevo insumo registrado"
                return HttpResponseRedirect('/products/productos_list/')
            else:
                print(form_class)
                contexto = {
                    'form': form_class
                }
            
        
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
    # fecha_inicial = filtros.POST['query']
    # fecha_final = filtros.POST['query2']

    # productos = Productos.objects.filter(
    #     fecha_creacion__gte=fecha_inicial,
    #     fecha_creacion__lte=fecha_final
    # ).order_by('-fecha_creacion')
    productos = Productos.objects.all().order_by('-fecha_creacion')
    return productos


def secciones_bodega(request):
    if request.method == 'POST' and "bodega_id" in request.POST:
        bodega_id = request.POST["bodega_id"]
        if bodega_id not in ('', None):
            secciones = Secciones.objects.filter(bodega_id = bodega_id)
            return JsonResponse([{'id':'0', 'descripcion':'Escoger una Seccion'}] + [{'id': seccion.id_seccion, 'descripcion':seccion.descripcion} for seccion in secciones], safe=False)
        else:
            return JsonResponse([{'id':'', 'descripcion':'Escoger una Seccion'}], safe=False)
    else:
        return HttpResponseBadRequest("Se ha realizado un mal requerimiento")



def validar_cantidad_produccion(request):
    if request.is_ajax and request.method == 'GET':
        id_insumo = request.GET['id_insumo']
        if id_insumo:
            insumo_obj = Productos.objects.filter(id_producto=id_insumo).first()
            data = {
                'cantidad_existente':  insumo_obj.cantidad_existente,
                'descripcion': insumo_obj.descripcion
            }
            return JsonResponse({'data': data}, status=200)
        else:
            return JsonResponse({'mensaje': 'Insumo no existe, por favor verifique'}, status=500)







def categorias_insumos_list(request):
    template_name = 'prd/categorias_insumos_list.html'
    contexto = {
        'categorias': CategoriaProducto.objects.all()
    }
    return render(request, template_name, contexto)


def actualizar_categoria_insumo(request, id_categoria=None):
    template_name = 'prd/actualizar_categoria_modal.html'
    contexto={}
    categoria = CategoriaProducto.objects.filter(id_categoria=id_categoria).first()

    if request.method == 'GET':
        contexto = {
            'categoria': categoria
        }
    else:
        json_data = json.loads(request.body)
        estado = json_data['estado']

        if estado == 'ACTIVO':
            estado = Estados.objects.filter(descripcion='INACTIVO').first()
        if estado == 'INACTIVO':
            estado = Estados.objects.filter(descripcion='ACTIVO').first()
        categoria.estado = estado
        categoria.save()
        return HttpResponse('Categoria de Proveedor Actualizada')
    
    return render(request, template_name, contexto)


def editar_categoria(request):
    if request.method == 'GET':
        descripcion = request.GET['descripcion']
        id_categoria = request.GET['categoria_id']

        if id_categoria != '0':
            categoria_obj = CategoriaProducto.objects.filter(id_categoria=id_categoria).first()
            categoria_obj.descripcion = descripcion
            categoria_obj.save()
            estado = True

            return JsonResponse({'mensaje': 'Categoria Editada', 'estado': estado}, status=200)
        else:
            infoCategoria = CategoriaProducto(
                descripcion = descripcion,
                usuario_crea=request.user.pk,
                usuario_modifica=request.user.pk,
                estado = Estados.objects.filter(descripcion__iexact='ACTIVO').first()
            )
            if infoCategoria:
                infoCategoria.save()
            estado = True
            return JsonResponse({'mensaje': 'Categoria Creada', 'estado': estado}, status=200)



def unidades_medidas_list(request):
    template_name = 'prd/unidades_medidas_list.html'
    contexto = {
        'unidades': UnidadMedida.objects.all()
    }
    return render(request, template_name, contexto)




def actualizar_unidad_medida(request, id_categoria=None):
    template_name = 'prd/actualizar_unidad_modal.html'
    contexto={}
    medida = UnidadMedida.objects.filter(id_categoria=id_categoria).first()

    if request.method == 'GET':
        contexto = {
            'medida': medida
        }
    else:
        json_data = json.loads(request.body)
        estado = json_data['estado']

        if estado == 'ACTIVO':
            estado = Estados.objects.filter(descripcion='INACTIVO').first()
        if estado == 'INACTIVO':
            estado = Estados.objects.filter(descripcion='ACTIVO').first()
        medida.estado = estado
        medida.save()
        return HttpResponse('Unidad de Medida Actualizada')
    
    return render(request, template_name, contexto)


def editar_unidad_medida(request):
    if request.method == 'GET':
        descripcion = request.GET['descripcion']
        id_categoria = request.GET['categoria_id']

        if id_categoria != '0':
            medida_obj = UnidadMedida.objects.filter(id_categoria=id_categoria).first()
            medida_obj.descripcion = descripcion
            medida_obj.save()
            estado = True

            return JsonResponse({'mensaje': 'Unidad Medida Editada', 'estado': estado}, status=200)
        else:
            infoCategoria = UnidadMedida(
                descripcion = descripcion,
                usuario_crea=request.user.pk,
                usuario_modifica=request.user.pk,
                estado = Estados.objects.filter(descripcion__iexact='ACTIVO').first()
            )
            if infoCategoria:
                infoCategoria.save()
            estado = True
            return JsonResponse({'mensaje': 'Unidad Medida Creada', 'estado': estado}, status=200)
