from django.db import models
from bases.models import *
# Create your models here.

class CategoriaPersonal(ClaseModelo):
    id_categoria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=350)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    class Meta:
        permissions = {
            ('crear_categoria_personal', ('Crear Categoria Personal')),
            ('editar_categoria_personal', ('Editar Categoria Personal')),
            ('actualizar_categoria_personal', ('Actualizar Categoria Personal')),
        }


class TipoPersonal(ClaseModelo):
    id_tipo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=350)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        permissions = {
            ('crear_tipo_personal', ('Crear Tipo Personal')),
            ('editar_tipo_personal', ('Editar Tipo Personal')),
            ('actualizar_tipo_personal', ('Actualizar Tipo Personal')),
        }


class PersonalFinca(ClaseModelo):
    id_personal = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=350)
    apellidos = models.CharField(max_length=350)
    
    def __str__(self):
        return '{} {} - {}'.format(
            self.nombres,
            self.apellidos
        )




# class CategoriaProveedor(ClaseModelo):
#     id_categoria = models.AutoField(primary_key=True)
#     descripcion = models.CharField(max_length=350)
#     estado = models.ForeignKey(Estados, on_delete=models.CASCADE, blank=True)

#     def __str__(self):
#         return '{}'.format(self.descripcion)
    
#     class Meta:
#         permissions = {
#             ('crear_categoria_proveedor', ('Crear Categoria Proveedor')),
#             ('editar_categoria_proveedor', ('Editar Categoria Proveedor')),
#             ('actualizar_categoria_proveedor', ('Actualizar Categoria Proveedor')),
#         }



# class Proveedores(ClaseModelo):
#     id_proveedor = models.AutoField(primary_key=True)
#     primer_nombre = models.CharField(max_length=350)
#     segundo_nombre = models.CharField(max_length=350)
#     primer_apellido = models.CharField(max_length=350)
#     segundo_apellido = models.CharField(max_length=350)
#     direccion = models.CharField(max_length=400)
#     telefono = models.CharField(max_length=15)
#     categoria = models.ForeignKey(CategoriaProveedor, on_delete=models.CASCADE, blank=True, null=True)
#     estado = models.ForeignKey(Estados, on_delete=models.CASCADE, blank=True)
#     def __str__(self):
#         return '{} {} - {}'.format(
#             self.primer_nombre,
#             self.primer_apellido,
#             self.categoria
#         )
#     class Meta:
#         permissions = {
#             ('crear_proveedor', ('Crear Proveedor')),
#             ('editar_proveedor', ('Editar Proveedor')),
#             ('actualizar_proveedor', ('Actualizar Proveedor')),
#         }