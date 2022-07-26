import json
from random import choice

from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponseRedirect, JsonResponse, HttpResponse
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy

from usr.models import *
from usr.serializers import *
from usr.forms import *
# Create your views here.

def usuarios_list(request):
    """obtener el listado de usuarios por pais"""
    if request.user.is_authenticated:
        template_name = "usr/usuarios_lista.html"
        # queryset usuarios
        if request.user.is_superuser:
            usuarios_obj = Usuarios.objects.all().exclude(pk=request.user.pk)
        else:
            usuarios_obj = Usuarios.objects.filter(is_superuser=False).\
                exclude(pk=request.user.id)
        contexto = {
            'usuarios': usuarios_obj
        }
        return render(request, template_name, contexto)
    else:
        return HttpResponseRedirect('/login/')


def roles_list(request):
    template_name = "usr/roles_lista.html"
    if request.user.is_authenticated:
        if request.user.is_superuser:
            roles = Roles.objects.filter(estado__descripcion='ACTIVO').exclude(descripcion='ADMINISTRADOR')
        else:
            roles = Roles.objects.filter(usuario_crea=request.user.id, tipo_usuario_id = request.user.tipo_usuario_id)
        context={
            'roles': roles
        }
        return render(request, template_name, context)
    else:
        return HttpResponseRedirect('/')


def RolesPermisos(request, rol_id=None):
    template_name = "usr/roles_form.html"
    rol_obj = Roles.objects.filter(id_rol=rol_id).first()
    grupo = Group.objects.filter(name="ADMINISTRADOR").first()
    permisos_admin = GruposPermisos.objects.filter(group=grupo)

    contenidos = []
    modulos = []

    for permiso in permisos_admin:
        tmp = []
        tmp.append(permiso.permission.content_type.model)
        tmp.append(permiso.permission.content_type.app_label)
        contenidos.append(tmp)
        modulo_tmp = permiso.permission.content_type.app_label
        convertidor = {
            'usr': 'Usuarios',
            'personal': 'Empleados',
            'ubc': 'Ubicaciones',
            'bases': 'Configuracion'
        }
        modulo = convertidor.get(modulo_tmp, 'ninguno')
        modulos.append([modulo_tmp, modulo])
    contenidos = set(map(tuple, contenidos))
    contenidos = sorted(contenidos)
    modulos = set(map(tuple, modulos))
    modulos = sorted(modulos)

    form_class = RolForm
    contexto = {}

    if request.method == 'GET':
        permisos_rol = []

        if rol_obj:
            
            permisos_asignados = GruposPermisos.objects.filter(group=rol_obj.grupo)
            for permiso in permisos_asignados:
                permisos_rol.append(str(permiso.permission_id))
            
            permisos_asignados = json.dumps(permisos_rol)
            form_class = RolForm(instance=rol_obj)

        else:
            permisos_asignados = None

        contexto = {
            'permisos_admin': permisos_admin,
            'rol': rol_obj,
            'contenidos': contenidos,
            'modulos': modulos,
            'permisos_asignados': permisos_asignados,
            'form': form_class
        }
    else:
        
        descripcion_rol = request.POST['descripcion']
        pais = str(request.user.pais.descripcion)
        permisos = request.POST.getlist('permisos[]')
        permisos_lista = json.loads(permisos[0])
        nombre_rol_grupo = descripcion_rol+'_'+pais

        if not rol_obj:
            infoGroup = Group(
                name=nombre_rol_grupo
            )
            try:
                infoGroup.save()
            except IntegrityError as e:
                return JsonResponse(
                    {'mensaje': str(e.__cause__)},
                    status=500
                )

            # crear rol
            infoRol = Roles(
                descripcion=descripcion_rol,
                grupo=infoGroup,
                usuario_crea=request.user.id,
                usuario_modifica = request.user.id,
                tipo_usuario_id = request.user.tipo_usuario_id
            )
            if infoRol:
                infoRol.save()
                for permiso in permisos_lista:
                    if permiso != 'on' and permiso != '0':
                        infoPermiso = GruposPermisos(
                            group_id = infoRol.grupo_id,
                            permission_id=permiso
                        )
                        infoPermiso.save()
        else:
            
            rol_obj.descripcion = descripcion_rol
            rol_obj.usuario_modifica = request.user.id
            rol_obj.save()

            permisos_grupo = GruposPermisos.objects.\
                filter(
                    group_id=rol_obj.grupo_id
                )
            if permisos_grupo:
                for permiso_grupo in permisos_grupo:
                    permiso_grupo.delete()

            for permiso in permisos_lista:
                if permiso != 'on' and permiso != '0':
                    infoPermiso = GruposPermisos(
                        group_id = rol_obj.grupo_id,
                        permission_id=permiso
                    )
                    infoPermiso.save()

    return render(request, template_name, contexto)


def editar_perfil(request, id_usuario=None): 
    template_name = 'usr/editar_perfil.html'
    contexto = {}
    perfil = Usuarios.objects.filter(pk=id_usuario).first()
    print(perfil)
    form_class = UsuarioGrupoForm
    if request.method == 'GET':
        if perfil:
            form_class = UsuarioGrupoForm(instance={'usuario':perfil})
        excluir_roles = ['ADMINISTRADOR', 'PROVEEDOR']
        roles = Roles.objects.filter(usuario_crea=request.user.id).exclude(descripcion__in=excluir_roles)
        print(roles)
        
        contexto ={
            'form': form_class,
            'obj': perfil,
            'roles': roles
        }
    if request.method == 'POST':
        rol = None
        if perfil:
            print('*****')
            print(request.FILES)
            prefijo_pais = request.user.pais.prefijo_cel
            img_perfil = None
            username = request.POST['usuario-username']
            nombres = request.POST['usuario-first_name']
            apellidos = request.POST['usuario-last_name']
            telefono = request.POST['usuario-telefono']
            correo = request.POST['usuario-email']
            user_telegram = request.POST['usuario-usuario_telegram']
            id_rol = request.POST['usuario-rol']
            
            telefono = str(prefijo_pais)+telefono[-9:]

            usuario = Usuarios.objects.filter(username=username).first()
            if id_rol:
                rol = Roles.objects.filter(id_rol=id_rol).first()
            else:
                rol = Roles.objects.filter(id_rol=usuario.rol_id).first()

            
            if Usuarios.objects.filter(email=correo).exclude(id=usuario.id).exists():
                return JsonResponse({
                    'mensaje': 'Correo ya se encuentra registrado.'
                }, status=500)
        
            if request.FILES:
                img_perfil = request.FILES['img_perfil']
                perfil.img_perfil = img_perfil
            perfil.first_name = nombres
            perfil.last_name = apellidos
            perfil.telefono = telefono
            perfil.email = correo
            perfil.usuario_telegram = user_telegram
            perfil.rol = rol
#            perfil.tipo_usuario_id = request.tipo_usuario_id
            perfil.save()

            grupoUsuario = UsuariosGrupos.objects.filter(usuarios_id=perfil.id).first()
            if grupoUsuario:
                grupoUsuario.group = rol.grupo
                grupoUsuario.save()
            else:
                infoGrupoUsuario = UsuariosGrupos(
                    usuarios_id = perfil.id,
                    group_id = rol.grupo_id
                )
                infoGrupoUsuario.save()

            return JsonResponse({
                    'correo': perfil.email,
                    'redireccion': 2
                })
        else:
            print(request.POST)

            username = request.POST['usuario-username']
            nombres = request.POST['usuario-first_name']
            apellidos = request.POST['usuario-last_name']
            telefono = request.POST['usuario-telefono']
            correo = request.POST['usuario-email']
            usuario_telegram = request.POST['usuario-usuario_telegram']
            rol = request.POST['usuario-rol']
            tipo_usuario = request.POST['usuario-tipo_usuario']

            if not username:
                return JsonResponse({
                    'mensaje': 'Ingrese el username.'
                }, status=500)  
            
            if not nombres:
                return JsonResponse({
                    'mensaje': 'Ingrese los nombres.'
                }, status=500)
            if not apellidos:
                return JsonResponse({
                    'mensaje': 'Ingrese los apellidos.'
                }, status=500)
            
            if not telefono:
                return JsonResponse({
                    'mensaje': 'Ingrese el numero telefonico'
                }, status=500)
            
            if not correo:
                return JsonResponse({
                    'mensaje': 'Ingrese el correo.'
                }, status=500)
            
            if not rol:
                return JsonResponse({
                    'mensaje': 'Seleccione un rol.'
                }, status=500)  
             

            if Usuarios.objects.filter(username=username).exists():
                return JsonResponse({
                    'mensaje': 'Username ya se encuentra en uso.'
                }, status=500)

            if Usuarios.objects.filter(email=correo).exists():
                return JsonResponse({
                    'mensaje': 'Correo ya se encuentra registrado.'
                }, status=500)
            if not tipo_usuario:
                return JsonResponse({
                    'mensaje': 'Seleccione tipo e usuario.'
                }, status=500)  
            


            # setear pasword 
            longitud = 6
            valores = '123456789' + \
                'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            tmp_pass = ""
            tmp_pass = tmp_pass.\
                join([choice(valores) for i in range(longitud)])
            
            tmp_pass.replace(" ", "")

            password = make_password(tmp_pass, salt=None, hasher='default')


            infoUsuario = Usuarios(
                username = username,
                first_name = nombres,
                last_name = apellidos,
                telefono = telefono,
                email = correo,
                usuario_telegram = usuario_telegram,
                rol_id = rol,
                password=password,
                is_superuser=False,
                tipo_usuario_id = request.user.tipo_usuario_id

            )
            if infoUsuario:
                infoUsuario.save()
                if request.FILES:
                    img_perfil = request.FILES['img_perfil']
                    infoUsuario.img_perfil = img_perfil
                    infoUsuario.save()
                return JsonResponse({
                    'correo': infoUsuario.email,
                    'redireccion': 1
                })
    return render(request, template_name, contexto)


def actualizar_perfil(request, pk):
    template_name = 'usr/actualizar_usuario_modal.html'
    contexto = {}
    usuario = Usuarios.objects.filter(id=pk).first()
    if request.method == 'GET':
        contexto = {
            'usuario': usuario
        }

    else:
        json_data = json.loads(request.body)
        print(json_data)
        estado = json_data['estado']

        if estado == 'ACTIVO':
            estado = Estados.objects.filter(descripcion='INACTIVO').first()
        if estado == 'INACTIVO':
            estado = Estados.objects.filter(descripcion='ACTIVO').first()
        usuario.estado = estado
        usuario.save()
        return HttpResponse('Usuario Actualizado')
    return render(request, template_name, contexto)


class EditUser(LoginRequiredMixin, generic.UpdateView):

    model = Usuarios
    template_name = "usr/editar_usuario.html"
    context_objects_name = "usuario"
    form_class = EditarUsuarioForm
    success_url = reverse_lazy('bases:inicio')
    login_url = 'bases:login'

# def EditUser(request, pk=None):
#     template_name = "usr/editar_usuario.html"
#     form = EditarUsuarioForm
#     usuario_obj = Usuarios.objects.filter(id=pk).first()


#     if request.method == 'GET':
#         print(pk)
#         contexto = {
#             'form': EditarUsuarioForm(instance=usuario_obj)
#         }

#     if request.method == 'POST':
#         imagen_perfil = request.POST['img_perfil']
#         username = request.POST['username']
#         nombres = request.POST['first_name']
#         apellidos = request.POST['last_name']
#         correo = request.POST['email']
#         telefono = request.POST['telefono']
#         usuario_telegram = request.POST['usuario_telegram']

#         usuario_obj.username = username
#         usuario_obj.first_name = nombres
#         usuario_obj.last_name = apellidos
#         usuario_obj.email = correo
#         usuario_obj.telefono = telefono
#         usuario_obj.usuario_telegram = usuario_telegram

#         usuario_obj.save()


        
    
#     return render(request, template_name, contexto)


def obtener_usuarios_bodega(request):
    if request.method == 'GET':
        #obtener los usuarios con rol bodeguero
        usuarios = Usuarios.objects.filter(rol__descripcion__iexact='BODEGUERO')
        serializer = UsuariosBodegueroSerializer(usuarios, many=True).data
        return JsonResponse({'data': serializer})