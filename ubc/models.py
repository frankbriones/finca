from django.db import models
from bases.models import *

# Create your models here.
class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=150)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE,blank=True, default=1)
    prefijo_cel = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Pais, self).save()
    class Meta:
        permissions = {
            ('crear_pais', ('Crear Pais')),
            ('editar_pais', ('Editar Pais')),
            ('actualizar_pais', ('Actualizar Pais')),
        }



class Ciudades(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=150)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, blank=True)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE,blank=True, default=1)
    codigo_api_ciudad = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Ciudades, self).save()
    
    class Meta:
        permissions = {
            ('crear_ciudades', ('Crear Ciudad')),
            ('editar_ciudades', ('Editar Ciudad')),
            ('actualizar_ciudades', ('Actualizar Ciudad')),
        }


class Bodegas(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=150)
    ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE, blank=True)
    direccion1 = models.CharField(max_length=150)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE,blank=True, default=1)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Bodegas, self).save()
    class Meta:
        permissions = {
            ('crear_bodega', ('Crear Bodega')),
            ('editar_bodega', ('Editar Bodega')),
            ('actualizar_bodega', ('Actualizar Bodega')),
        }


class Secciones(models.Model):
    id_seccion = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=150)
    bodega = models.ForeignKey(Bodegas, on_delete=models.CASCADE, blank=True)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE,blank=True, default=1)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Secciones, self).save()
    class Meta:
        permissions = {
            ('crear_bodega', ('Crear Bodega')),
            ('editar_bodega', ('Editar Bodega')),
            ('actualizar_bodega', ('Actualizar Bodega')),
        } 



class Sectores(ClaseModelo):
    # modelo para informacion de sectores dentro de la finca
    # ejemplo finca la gloria
    id_sector = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=150)
    ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE, blank=True)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE,blank=True, default=1)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Sectores, self).save()
    
    class Meta:
        permissions = {
            ('crear_sectores', ('Crear Sectores')),
            ('editar_sectores', ('Editar Sectores')),
            ('actualizar_sectores', ('Actualizar Sectores')),
        }


class Lotes(ClaseModelo):
    id_lote = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=150)
    sector = models.ForeignKey(Sectores, on_delete=models.CASCADE, blank=True)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE,blank=True, default=1)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Lotes, self).save()
    
    class Meta:
        permissions = {
            ('crear_lotes', ('Crear Lotes')),
            ('editar_lotes', ('Editar Lotes')),
            ('actualizar_lotes', ('Actualizar Lotes')),
        }