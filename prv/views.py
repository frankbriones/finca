import json
from datetime import datetime, timezone
from unittest import installHandler
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
from random import choice

from rest_framework.views import APIView


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse

from .models import *
from usr.models import *
from .forms import *
from .serializers import *
from .resources import *
# Create your views here.

def proveedores_list(request):
    template_name = 'prv/proveedores_list.html'
    contexto = {
        'proveedores': Proveedores.objects.filter(pais_id=request.user.pais_id)
    }
    return render(request, template_name, contexto)



@login_required(login_url='/login/')
def actualizar_proveedor_personal(request, id_proveedor=None):
    template_name = 'prv/actualizar_proveedor_modal.html'
    contexto={}
    proveedor = Proveedores.objects.filter(id_proveedor=id_proveedor).first()

    if request.method == 'GET':
        contexto = {
            'proveedor': proveedor
        }
    else:
        json_data = json.loads(request.body)
        estado = json_data['estado']

        if estado == 'ACTIVO':
            estado = Estados.objects.filter(descripcion='INACTIVO').first()
        if estado == 'INACTIVO':
            estado = Estados.objects.filter(descripcion='ACTIVO').first()
        proveedor.estado = estado
        proveedor.save()
        return HttpResponse('Proveedor Actualizado')
    
    return render(request, template_name, contexto)



@login_required(login_url='/login/')
def editar_proveedor_modal(request, id_proveedor=None):
    template_name = 'prv/editar_proveedor_modal.html'
    contexto={}
    form_class = ProveedoresForm()
    proveedor = Proveedores.objects.filter(id_proveedor=id_proveedor).first()
    categorias = CategoriaProveedor.objects.all()
    categorias_disponibles = [categoria.categoria.id_categoria for categoria in CategoriasProveedor.objects.filter(proveedor_id=id_proveedor)]
        
    if request.method == 'GET':
        if proveedor:
            form_class = ProveedoresForm(
                initial = {
                    'identificacion': proveedor.identificacion,
                    'nombres': proveedor.nombres,
                    'apellidos': proveedor.apellidos,
                    'telefono': proveedor.telefono,
                    'correo': proveedor.correo,
                    'direccion': proveedor.direccion,
                    'ciudad': proveedor.ciudad,
                    'usuario': proveedor.usuario
                }
            )
        
        contexto = {
            'proveedor': proveedor,
            'form': form_class,
            'categorias': categorias,
            'categorias_disponibles': categorias_disponibles
        }

    else:
        print(request.POST)
        identificacion = request.POST['identificacion']
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        ciudad_id = request.POST['ciudad']
        usuario_obj = {}
        
        if not proveedor:
            username = request.POST['usuario']
            usuario_obj = Usuarios.objects.filter(username__iexact=username).first()
            if not username:
                return JsonResponse({
                        'mensaje': "Ingrese el username"
                    }, status=500)
            if Usuarios.objects.filter(username=username).exists():
                return JsonResponse({
                        'mensaje': "Nombre de usuario esta en uso"
                    }, status=500)
            else:
                if Proveedores.objects.filter(usuario__username=username).exists():
                    return JsonResponse({
                        'mensaje': "Nombre de usuario no disponible"
                    }, status=500)
        else:
            try:

                username = proveedor.usuario.username
                usuario_obj = proveedor.usuario
            except AttributeError:
                return JsonResponse({
                        'mensaje': "Ingrese el nombre de ususario"
                    }, status=500)


        categorias = request.POST.getlist('categoriasDisponibles[]')
        categorias = json.loads(categorias[0])
        if len(identificacion) != 10:
            return JsonResponse({
                    'mensaje': 'Ingrese un numero de identificacion valido.'
                }, status=500)
        
        if len(identificacion) == 10:
            numeros = [ int(identificacion[x]) * (2 - x % 2) for x in range(9) ]
            suma = sum(map(lambda x: x > 9 and x - 9 or x, numeros))
            suma = int(identificacion[9]) == 10 - int(str(suma)[-1:])
            if suma is False:
                return JsonResponse({
                    'mensaje': 'Numero de identificacion invalido.'
                }, status=500)
        
        if not nombres:
            return JsonResponse({
                    'mensaje': 'Ingrese los nombres.'
                }, status=500)

        if not apellidos:
            return JsonResponse({
                    'mensaje': 'Ingrese los Apellidos.'
                }, status=500)
        
        if not telefono:
            return JsonResponse({
                    'mensaje': 'Ingrese numero de telefono.'
                }, status=500)
        if not direccion:
            return JsonResponse({
                    'mensaje': 'Ingrese la Direccion.'
                }, status=500)
        if not correo:
            return JsonResponse({
                    'mensaje': 'Ingrese el correo.'
                }, status=500)
        else:
            if(len(correo) < 5):
                return JsonResponse({
                        'mensaje': 'correo no valido'
                    }, status=500)
        if not ciudad_id:
            return JsonResponse({
                    'mensaje': 'Seleccion una ciudad'
                }, status=500)

            

        estado_peticion = False

        if Proveedores.objects.filter(identificacion=identificacion).exclude(id_proveedor=id_proveedor).first():
                return JsonResponse({'mensaje': 'Identificacion ya existe', 'estado': estado_peticion})
        if Proveedores.objects.filter(correo=correo).exclude(id_proveedor=id_proveedor).first():
            return JsonResponse({'mensaje': 'Correo ya existe', 'estado' : estado_peticion})
        
        
        rol_insumos = Roles.objects.filter(descripcion='PROVEEDOR').first()

        longitud = 6
        valores = "0123456789" + \
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        tmp_pass = ""
        tmp_pass = tmp_pass.\
            join([choice(valores) for i in range(longitud)])
        tmp_pass.replace(" ", "")

        password = make_password(tmp_pass, salt=None, hasher='default')

        if not usuario_obj:
            usuario_obj = Usuarios(
                first_name = nombres,
                last_name=apellidos,
                email=correo,
                pais_id=request.user.pais_id,
                telefono=telefono,
                rol=rol_insumos,
                estado=Estados.objects.filter(descripcion='ACTIVO').first(),
                username=username,
                password=password,
                tipo_usuario = TipoUsuario.objects.filter(descripcion='USUARIO INSUMOS').first()

            )
            if usuario_obj:
                usuario_obj.save()
            infoGrupoUsuario = UsuariosGrupos(
                usuarios_id = usuario_obj.id,
                group_id = rol_insumos.grupo_id
            )
            infoGrupoUsuario.save()
            
                
            

        
        if proveedor:
            proveedor.identificacion = identificacion
            proveedor.nombres = nombres
            proveedor.apellidos = apellidos
            proveedor.telefono = telefono
            proveedor.direccion = direccion
            proveedor.correo = correo
            proveedor.ciudad_id = ciudad_id
            proveedor.usuario_id = usuario_obj.id
            proveedor.save()
            estado_peticion = True
            antiguas_categorias = CategoriasProveedor.objects.filter(proveedor_id=proveedor.id_proveedor)
            for c in antiguas_categorias:
                c.delete()

            if categorias:
                for id_categoria in categorias:
                    infoCategoria = CategoriasProveedor(
                        proveedor=proveedor,
                        categoria_id = id_categoria
                    )
                    infoCategoria.save()

            return JsonResponse({'mensaje': 'Informacion Editada', 'estado' : estado_peticion})
        else:
            estado_peticion = True

            infoProveedor = Proveedores(
                identificacion = identificacion,
                nombres = nombres,
                apellidos = apellidos,
                telefono = telefono,
                direccion = direccion,
                correo = correo,
                ciudad_id = ciudad_id,
                usuario_crea = request.user.id,
                usuario_modifica = request.user.id,
                estado_id = 1,
                pais_id = request.user.pais_id,
                usuario=usuario_obj
            )
            
            if infoProveedor:
                infoProveedor.save()
            if categorias:
                for id_categoria in categorias:
                    infoCategoria = CategoriasProveedor(
                        proveedor=infoProveedor,
                        categoria_id = id_categoria
                    )
                    infoCategoria.save()
            return JsonResponse({'mensaje': 'Proveedor Ingresado', 'estado' : estado_peticion, 'correo': infoProveedor.correo})
           
    return render(request, template_name, contexto)


# #pruebas
# def nuevo_estudiante(request, estudiante_id = None):
# 	template ='taller/nuevo_estudiante.html'

# 	form = SignupForm()
# 	estudiante= None
	
# 	if request.method == 'POST':
# 		form = SignupForm(request.POST, request.FILES)
# 		(form.data)
# 		if form.is_valid():
# 			estudiante = form.save()
# 			request.session['msge'] = "Ingreso de Estudiante Realizado!"
# 			return HttpResponseRedirect(reverse('tallers:taller'))
# 	return render(request, template, {'form':form})


@login_required(login_url='/login/')
def proveedores_ajax(request):
    proveedores = Proveedores.objects.filter(estado__descripcion='ACTIVO')
    serializers = ProveedoresSerializer(proveedores, many=True).data
    return JsonResponse({'proveedores': serializers})




class ProveedoresReporte(APIView):
    def post(self, request):
        filtros = self.request
        print(filtros)
        proveedores = BusquedaProveedores(
            filtros
        )
        proveedores_lista = []
        if proveedores:
            ahora = datetime.now(timezone.utc)
            for proveedor in proveedores:
                proveedores_lista.append(proveedor)
            proveedor_resource = ProveedoresResource()
            dataset = proveedor_resource.export(proveedores_lista)
            nombre_archivo = 'Reporte_Proveedores_' + \
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


def BusquedaProveedores(filtros):
    fecha_inicial = filtros.POST['query']
    fecha_final = filtros.POST['query2']

    proveedores = Proveedores.objects.filter(
        estado__descripcion='ACTIVO',
        fecha_creacion__gte=fecha_inicial,
        fecha_creacion__lte=fecha_final
    ).order_by('-fecha_creacion')

    return proveedores