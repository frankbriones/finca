from django.db import models


# Create your models here.
class ClaseModelo(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_crea = models.IntegerField(blank=True,
                                        null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_modifica = models.IntegerField(blank=True)

    class Meta:
        abstract  = True

class Estados(models.Model):
    id_estado = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.descripcion)
        
    
class ConfiguracionSistema(models.Model):
    clave = models.CharField(max_length=200)
    valor = models.CharField(max_length=200)
    