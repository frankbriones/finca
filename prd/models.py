from django.db import models

from bases.models import Estados, ClaseModelo
from ubc.models import *
from prv.models import *

# Create your models here.
#modelos de gestion de productos


class CategoriaProducto(ClaseModelo):
    id_categoria = models.AutoField(primary_key=True)
    descripcion  = models.CharField(max_length=200)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(CategoriaProducto, self).save()

    class Meta:
        permissions = {
            ('crear_categoria_prd', ('Crear Categoria Producto')),
            ('editar_categoria_prd', ('Editar Categoria Prducto')),
            ('actualizar_categoria_prd', ('Actualizar Categoria Prducto')),
        }



class UnidadMedida(ClaseModelo):
    id_categoria = models.AutoField(primary_key=True)
    descripcion  = models.CharField(max_length=200)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()

    class Meta:
        permissions = {
            ('crear_unidad_meidida', ('Crear Unidad Medida')),
            ('editar_unidad_meidida', ('Editar Unidad Medida')),
            ('actualizar_unidad_meidida', ('Actualizar Unidad Medida')),
        }


class Productos(ClaseModelo):
    id_producto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, blank=True)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE, blank=True)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, blank=True)
    cantidad_minima = models.IntegerField(default=1, blank=True, null=True)
    cantidad_existente = models.IntegerField(default=0, blank=True, null=True)
    bodega = models.ForeignKey(Bodegas, on_delete=models.CASCADE)
    seccion = models.ForeignKey(Secciones, on_delete=models.CASCADE)
    #proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Productos, self).save()
    
    class Meta:
        permissions = {
            ('crear_producto', ('Crear Producto')),
            ('editar_producto', ('Editar Prducto')),
            ('actualizar_producto', ('Actualizar Prducto')),
            ('solicitar_producto', ('Solicitar Producto a Proveedores')),

        }



# class ProveedorProducto(models.Model):
#     id_prv_prd = models.AutoField(primary_key=True)
#     producto = models.ForeignKey(Productos, on_delete=models.CASCADE, blank=True)
#     proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, blank=True)

#     def __str__(self):
#         return '{}-{}'.format(self.producto, self.proveedor)