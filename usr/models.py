from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

from bases.models import *
from ubc.models import *
# Create your models here.

class TipoUsuario(ClaseModelo):
    id_tipo = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(TipoUsuario, self).save()


class Roles(ClaseModelo):
    id_rol = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.ForeignKey(Estados,
                                on_delete=models.CASCADE,
                                default=1)
    grupo = models.ForeignKey(Group,
                            on_delete=models.CASCADE,
                            default=1)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, blank=True, null=True)
                                
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Roles, self).save()

    class Meta:
        permissions = {
            ('crear_rol', ('Crear Rol')),
            ('editar_rol', ('Editar Rol')),
            ('actualizar_rol', ('Actualizar Rol')),
        }






class Usuarios(AbstractUser):
    rol = models.ForeignKey(Roles,
                            on_delete=models.CASCADE,
                            default=1)
    estado = models.ForeignKey(Estados,
                                on_delete=models.CASCADE,
                                default=1)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)

    img_perfil = models.ImageField(upload_to='perfil_img',null=True, blank=True)

    telefono = models.CharField(max_length=20, blank=True, null=True)

    usuario_telegram = models.CharField(max_length=50, null=True, blank=True)

    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.username)
    
    class Meta:
        permissions = {
            ('crear_usuarios', ('Crear Usuarios')),
            ('editar_usuarios', ('Editar Usuarios')),
            ('actualizar_usuarios', ('Actualizar Usuarios')),
        }


class UsuariosGrupos(models.Model):
    usuarios = models.ForeignKey(Usuarios, models.DO_NOTHING)
    group = models.ForeignKey(Group, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usr_usuarios_groups'
        unique_together = (('usuarios', 'group'),)


class GruposPermisos(models.Model):

    group = models.ForeignKey(Group, models.DO_NOTHING)
    permission = models.ForeignKey(Permission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)
    