from django.db import models

# Create your models here.
from bases.models import *
from ubc.models import *

class CategoriaProveedor(ClaseModelo):
    id_categoria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=300)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(CategoriaProveedor, self).save()


from usr.models import Usuarios
class Proveedores(ClaseModelo):
    id_proveedor = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=30,null=False,blank=False)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    direccion = models.CharField(max_length=500)
    telefono = models.CharField(max_length=50, null=True)
    correo = models.EmailField(unique=True, null=True)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, blank=True, related_name='estado_prv')
    ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    #categoria = models.ForeignKey(CategoriaProveedor, on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.OneToOneField(Usuarios, on_delete=models.CASCADE, blank=True, null=True, related_name='proveedor')

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)
    
    def save(self):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Proveedores, self).save()

    class Meta:
        permissions = {
            ('crear_proveedor', ('Crear Proveedor')),
            ('editar_proveedor', ('Editar Proveedor')),
            ('actualizar_proveedor', ('Actualizar Proveedor')),
        }


class CategoriasProveedor(models.Model):
    id_categoria_proveedor = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, blank=True, null=True)
    categoria = models.ForeignKey(CategoriaProveedor, on_delete=models.CASCADE, blank=True, null=True)






# class Estudiante(models.Model):
#     class Meta:
#         permissions = [
#         ("add_persona", "Can change the status of tasks"),
#     ]



#     usuario = models.OneToOneField(Profile, null=True, blank=True, related_name='usuar', on_delete=models.CASCADE)
#     contador_taller = models.IntegerField(null=True)

#     def as_dict(self):
#         dic =self.__dict__
#         dic['email']= self.usuario.email
#         return dic

#     def get_absolute_url(self):
#         return reverse("talleres:detalle_estudiante" , kwargs={'estudiante_id': self.pk})

#     def __str__(self):
#         return '{} {}'.format(self.usuario.nombres, self.usuario.apellidos) 


