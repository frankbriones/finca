import json

from django.shortcuts import render
from django.http.response import HttpResponseRedirect, JsonResponse, HttpResponse

from prd.models import Productos
from prd.resources import ProductoResource

from ubc.models import *
from ubc.forms import *
from ubc.serializers import *

# Create your views here.
def pais_list(request):
    if request.user.is_authenticated:
        template_name = 'ubc/pais_list.html'
        contexto = {
            'paises': Pais.objects.all()
        }
        return render(request, template_name, contexto)
    else:
        return HttpResponseRedirect('/login/')


def ciudad_list(request):
    if request.user.is_authenticated:
        template_name = 'ubc/ciudades_list.html'
        contexto = {
            'ciudades': Ciudades.objects.filter(pais_id=request.user.pais_id)
        }
        return render(request, template_name, contexto)
    else:
        return HttpResponseRedirect('/login/')



def sectores_list(request):
    if request.user.is_authenticated:
        template_name = 'ubc/sectores_list.html'
        contexto = {
            'sectores': Sectores.objects.filter(ciudad__pais_id=request.user.pais_id)
        }
        return render(request, template_name, contexto)
    else:
        return HttpResponseRedirect('/login/')


def bodegas_list(request):
    if request.user.is_authenticated:
        template_name = 'ubc/bodegas_list.html'
        contexto = {
            'bodegas': Bodegas.objects.all()
        }
        return render(request, template_name, contexto)
    else:
        return HttpResponseRedirect('/')

def lotes_list(request):
    if request.user.is_authenticated:
        template_name = 'ubc/lotes_list.html'
        contexto = {
            'lotes': Lotes.objects.filter(sector__ciudad__pais_id=request.user.pais_id)
        }
        return render(request, template_name, contexto)
    else:
        return HttpResponseRedirect('/login/')




def actualizar_pais(request, id_pais=None):
    template_name = 'ubc/actualizar_pais_modal.html'
    contexto = {}
    pais = Pais.objects.filter(id_pais=id_pais).first()
    if request.method == 'GET':
        contexto = {
            'pais': pais
        }

    else:
        json_data = json.loads(request.body)
        estado = json_data['estado']

        if estado == 'ACTIVO':
            estado = Estados.objects.filter(descripcion='INACTIVO').first()
        if estado == 'INACTIVO':
            estado = Estados.objects.filter(descripcion='ACTIVO').first()
        pais.estado = estado
        pais.save()
        return HttpResponse('Pais Actualizado')
    return render(request, template_name, contexto)



def actualizar_ciudad(request, id_ciudad=None):
    template_name = 'ubc/actualizar_ciudad_modal.html'
    contexto = {}
    ciudad = Ciudades.objects.filter(id_ciudad=id_ciudad).first()
    if request.method == 'GET':
        contexto = {
            'ciudad': ciudad
        }

    else:
        json_data = json.loads(request.body)
        estado = json_data['estado']

        if estado == 'ACTIVO':
            estado = Estados.objects.filter(descripcion='INACTIVO').first()
        if estado == 'INACTIVO':
            estado = Estados.objects.filter(descripcion='ACTIVO').first()
        ciudad.estado = estado
        ciudad.save()
        return HttpResponse('Ciudad Actualizada')
    return render(request, template_name, contexto)



def actualizar_sector(request, id_sector=None):
    template_name = 'ubc/actualizar_sector_modal.html'
    contexto = {}
    sector_obj = Sectores.objects.filter(id_sector=id_sector).first()
    if request.method == 'GET':
        contexto = {
            'sector': sector_obj
        }

    else:
        json_data = json.loads(request.body)
        estado = json_data['estado']

        if estado == 'ACTIVO':
            estado = Estados.objects.filter(descripcion='INACTIVO').first()
        if estado == 'INACTIVO':
            estado = Estados.objects.filter(descripcion='ACTIVO').first()
        sector_obj.estado = estado
        sector_obj.save()
        return HttpResponse('Sector Actualizado')
    return render(request, template_name, contexto)




def actualizar_lote(request, id_lote=None):
    template_name = 'ubc/actualizar_lote_modal.html'
    contexto = {}
    lote = Lotes.objects.filter(id_lote=id_lote).first()
    if request.method == 'GET':
        contexto = {
            'lote': lote
        }
    else:
        json_data = json.loads(request.body)
        estado = json_data['estado']

        if estado == 'ACTIVO':
            estado = Estados.objects.filter(descripcion='INACTIVO').first()
        if estado == 'INACTIVO':
            estado = Estados.objects.filter(descripcion='ACTIVO').first()
        lote.estado = estado
        lote.save()
        return HttpResponse('Lote Actualizado')
    return render(request, template_name, contexto)




def detalle_bodega(request, id_bodega=None):
    template_name = 'ubc/detalle_bodega.html'
    contexto = {}
    form_class = BodegaForm
    bodega = Bodegas.objects.filter(id_bodega=id_bodega).first()
    
    if request.method == 'GET':
        form_class = BodegaForm(instance=bodega)
        contexto = {
            'bodega': bodega,
            'form': form_class
        }
    else:
        print(request.POST)
        
        return HttpResponse('Bodega Ingresada')
    return render(request, template_name, contexto)



def secciones_bodega(request, id_bodega=None):
    if request.method == 'GET':
        if id_bodega:
            secciones = Secciones.objects.filter(bodega_id=id_bodega)
            serializer = SeccionesSerializer(secciones, many=True).data
            return JsonResponse({'secciones': serializer})


def editar_bodega(request, id_bodega=None):
    if request.is_ajax and request.method == 'GET':
        descripcion = request.GET['descripcion']
        direccion = request.GET['direccion']
        ciudad_id = request.GET['ciudad']
    
        secciones = request.GET.getlist('secciones[]')
        secciones = json.loads(secciones[0])
        if id_bodega:
            bodega_obj = Bodegas.objects.filter(id_bodega=id_bodega).first()
            bodega_obj.descripcion = descripcion
            bodega_obj.direccion1 = direccion
            bodega_obj.ciudad_id = ciudad_id
            bodega_obj.save()

            # for seccion in Secciones.objects.filter(bodega_id=bodega_obj.id_bodega):
            #     seccion.delete()

            for secc in secciones:
                print('xxxx', secc.get('descripcion'))
                try:
                    id_seccion = int(secc.get('id_seccion'))
                    seccion_obj = Secciones.objects.filter(id_seccion = secc.get('id_seccion')).exists()
                    if seccion_obj:
                        # return JsonResponse({'mensaje': 'Existen Secciones Repetidas', 'estado': False})

                        seccion = Secciones.objects.filter(id_seccion=secc.get('id_seccion')).first()
                        seccion.descripcion = secc.get('descripcion')
                        seccion.bodega_id = bodega_obj.id_bodega
                        seccion.save()
                except ValueError:
                    seccion_existe = Secciones.objects.filter(descripcion = secc.get('descripcion'), bodega_id=bodega_obj.id_bodega).exists()
                    if seccion_existe:
                        return JsonResponse({'mensaje': 'Existen Secciones Repetidas', 'estado': False})
                    if secc.get('descripcion') != None:
                        infoSeccion = Secciones(
                            descripcion = secc.get('descripcion'),
                            bodega_id = bodega_obj.id_bodega
                        )
                        if infoSeccion:
                            infoSeccion.save()
                    else:
                        pass
                
            return JsonResponse({'mensaje': 'Bodega Editada', 'estado': True})
        else:
            infoBodega = Bodegas(
                descripcion = descripcion,
                direccion1=direccion,
                ciudad_id=ciudad_id,
                estado=Estados.objects.filter(descripcion__iexact='ACTIVO').first()
            )
            if infoBodega:
                infoBodega.save()
                for secc in secciones:
                    try:
                        id_seccion = int(secc.get('id_seccion'))
                        seccion_obj = Secciones.objects.filter(id_seccion = secc.get('id_seccion')).exists()
                        if seccion_obj:
                            # return JsonResponse({'mensaje': 'Existen Secciones Repetidas', 'estado': False})

                            seccion = Secciones.objects.filter(id_seccion=secc.get('id_seccion')).first()
                            seccion.descripcion = secc.get('descripcion')
                            seccion.bodega_id = infoBodega.id_bodega
                            seccion.save()
                    except ValueError:
                        seccion_existe = Secciones.objects.filter(descripcion = secc.get('descripcion'), bodega_id=infoBodega.id_bodega).exists()
                        if seccion_existe:
                            return JsonResponse({'mensaje': 'Existen Secciones Repetidas', 'estado': False})
                        infoSeccion = Secciones(
                            descripcion = secc.get('descripcion'),
                            bodega_id = infoBodega.id_bodega
                        )
                        if infoSeccion:
                            infoSeccion.save()

            return JsonResponse({'mensaje': 'Bodega Registrada', 'estado': True})


def modal_editar_pais(request, id_pais=None):
    template_name = 'ubc/editar_pais_modal.html'
    contexto = {}
    if request.method == 'GET':
        if id_pais:
            pais_obj = Pais.objects.filter(id_pais=id_pais).first()
            contexto = {
                'pais': pais_obj
            }
    return render(request, template_name, contexto)



def editar_pais(request):
    if request.is_ajax:
        id_pais = request.GET['pais_id']
        descripcion = request.GET['descripcion']
        prefijo = request.GET['prefijo']
        if id_pais:
            pais_obj = Pais.objects.filter(id_pais=id_pais).first()
            pais_obj.descripcion = str(descripcion)
            pais_obj.prefijo_cel = str(prefijo)
            pais_obj.save()

            return JsonResponse({'mensaje': 'Pais editado'}, status=200)


def modal_crear_pais(request):
    template_name = 'ubc/crear_pais_modal.html'
    contexto = {}
    
    return render(request, template_name, contexto)


def crear_pais(request):
    if request.method == 'GET':
        descripcion = request.GET['descripcion']
        prefijo = request.GET['prefijo']

        infoPais = Pais(
            descripcion = descripcion,
            estado = Estados.objects.filter(descripcion__iexact='ACTIVO').first(),
            prefijo_cel= str(prefijo)
        )
        if infoPais:
            infoPais.save()
        return JsonResponse({'mensaje': 'Pais Creado'}, status=200)



def crear_bodega(request):
    template_name = "ubc/detalle_bodega.html"
    contexto = {}
    form = BodegaForm
    contexto = {
        'form': form
    }

    return render(request, template_name, contexto)



def detalle_ciudad(request, id_ciudad=None):
    template_name = 'ubc/detalle_ciudad.html'
    contexto = {}
    form_class = CiudadForm
    ciudad = Ciudades.objects.filter(id_ciudad=id_ciudad).first()
    
    if request.method == 'GET':
        form_class = CiudadForm(instance=ciudad)
        contexto = {
            'ciudad': ciudad,
            'form': form_class
        }
    else:
        descripcion = request.POST['descripcion']
        pais_id = request.POST['pais']
        if ciudad:
            ciudad.descripcion = descripcion
            ciudad.pais_id = pais_id
            ciudad.save()

            estado = True
            mensaje = 'Ciudad Editada'

        else:
            infoCiudad = Ciudades(
                descripcion=descripcion,
                pais_id=pais_id,
                estado=Estados.objects.filter(descripcion__iexact='ACTIVO').first(),
                codigo_api_ciudad=''
            )
            if infoCiudad:
                infoCiudad.save()
            estado=True
            mensaje = 'Ciudad Registrada'
        return JsonResponse({
            'mensaje': mensaje,
            'estado': estado
        }, status=200)
        
        
    return render(request, template_name, contexto)


def crear_ciudad(request):
    template_name = "ubc/detalle_ciudad.html"
    contexto = {}
    form = CiudadForm
    contexto = {
        'form': form
    }

    return render(request, template_name, contexto)



def eliminar_seccion_bodega(request):
    if request.is_ajax:
        id_seccion = request.GET['id_seccion']
        if id_seccion:
            producto_seccion = Productos.objects.filter(seccion_id = id_seccion).exists()
            if producto_seccion:
                return JsonResponse({'mensaje': 'No se puede eliminar la seccion, esta relacionada a uno o varios insumos.'}, status=500)
            else:
                seccion_obj = Secciones.objects.filter(id_seccion=id_seccion).first()
                seccion_obj.delete()
                return JsonResponse({'mensaje': 'seccion eliminada'}, status=200)