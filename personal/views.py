import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http.response import HttpResponseRedirect, JsonResponse, HttpResponse

from bases.models import Estados
from personal.models import PersonalFinca, TipoPersonal, CategoriaPersonal
from personal.serializers import CategoriaSerializers, PersonalSerializers

# Create your views here.

@login_required(login_url='/login/')
def empleados_list(request):
    template_name = 'personal/empleados_list.html'
    contexto = {}
    return render(request, template_name, contexto)


@login_required(login_url='/login/')
def tipos_empleado_list(request):
    template_name = 'personal/tipo_empleado_list.html'
    contexto = {
        'tipos': TipoPersonal.objects.filter(estado__descripcion='ACTIVO')
    }
    return render(request, template_name, contexto)




@login_required(login_url='/login/')
def categorias_empleado_list(request):
    template_name = 'personal/categoria_empleado_list.html'
    contexto = {
        'categorias': CategoriaPersonal.objects.all().order_by('-fecha_creacion')
    }
    return render(request, template_name, contexto)


@login_required(login_url='/login/')
def categorias_ajax(request):
    categorias = CategoriaPersonal.objects.filter(estado__descripcion='ACTIVO')
    serializers = CategoriaSerializers(categorias, many=True).data
    return JsonResponse({'categorias': serializers})


@login_required(login_url='/login/')
def listado_empleados_ajax(request):
    if request.is_ajax and request.method == 'GET':
        estados = request.GET['estadosBusqueda[]']
        estados = json.loads(estados)

        datos = (json.loads(json.dumps(request.GET)))
        categoria = request.GET['categoria_id']
        if categoria != None:
            categoria = request.GET['categoria_id']
        body = {
            'estados': estados,
            'claveBusqueda': datos['claveBusqueda'],
            'categoria_id': categoria
        }
        
        employee = obtenerEmpleados(body)
        serializer = PersonalSerializers(employee, many=True).data
        return JsonResponse({'empleados': serializer, 'registros': employee.count()})


def obtenerEmpleados(filtros):
    palabra_busqueda = filtros.get('claveBusqueda')
    estados = filtros.get('estados')
    categoria_id = filtros.get('categoria_id')
    tipos_id = {}
    if len(estados):
        tipos_id = TipoPersonal.objects.\
            filter(
                id_tipo__in = estados
            ).values('id_tipo')
    if len(tipos_id) >= 1:
        empleados = PersonalFinca.objects.\
            filter(
                tipo_id__in=tipos_id,
                categoria_id=categoria_id
            ).order_by('-fecha_creacion')
        if palabra_busqueda != None:
            empleados = empleados.\
                filter(
                    primer_nombre__icontains=palabra_busqueda
                ) | empleados.\
                filter(
                    primer_apellido__icontains = palabra_busqueda
                )
    else:
        empleados = PersonalFinca.objects.\
            filter(
                categoria_id=categoria_id
            ).order_by('-fecha_creacion')
        if palabra_busqueda != None:
            empleados = empleados.\
                filter(
                    primer_nombre__icontains=palabra_busqueda
                ) | empleados.\
                filter(
                    primer_apellido__icontains = palabra_busqueda
                )
    return empleados



def actualizar_categoria_personal(request, id_categoria=None):
    template_name = 'personal/actualizar_categoria_modal.html'
    contexto={}
    categoria = CategoriaPersonal.objects.filter(id_categoria=id_categoria).first()

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
        return HttpResponse('Categoria Actualizada')
    
    return render(request, template_name, contexto)


def editar_categoria(request):
    estado = False
    if request.method == 'GET':
        id_categoria = request.GET['categoria_id']
        descripcion = request.GET['descripcion']
        if id_categoria:
            categoria_obj = CategoriaPersonal.objects.filter(id_categoria=id_categoria).first()
            if categoria_obj:
                if descripcion != categoria_obj.descripcion:
                    categoria_obj.descripcion = descripcion
                    categoria_obj.save()
                    estado = True
                    mensaje = "Categoria Modificada"
                else:
                    mensaje = "Categoria Sin Modificar"
            return JsonResponse({'mensaje': mensaje, 'estado': estado})