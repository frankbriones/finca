from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from usr.views import *

app_name = 'usr'

urlpatterns = [
   path('list/', usuarios_list, name="usuarios_list"),
   path('usuaios/bodega/list', obtener_usuarios_bodega, name="obtener_usuarios_bodega"),
   path('roles/list/',roles_list, name="roles_list"),
   path('roles/crear/<int:rol_id>/', RolesPermisos, name="roles_crear"),
   path('editar-perfil/<int:id_usuario>', editar_perfil, name="editar_perfil"),
   path('editar-user/<int:pk>', EditUser.as_view(), name="edit_user"),#editar user logeado
   #path('editar-user/<int:pk>', EditUser, name="edit_user"),#editar user logeado

   path('actualizar-perfil/<int:pk>', actualizar_perfil, name="actualizar_perfil"),
   path('contrasena-nuevo-usuario/',
      auth_views.PasswordResetView.as_view(
         template_name='bases/contrasena_olvidada.html',
         email_template_name='usr/correo_nuevo_usuario.html',
         subject_template_name='usr/asunto_correo_usuario_nuevo.txt'
      ),
      name='contrasena_nuevo_usuario'
   )
]