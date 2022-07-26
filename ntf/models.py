from django.db import models

from bases.models import Estados
from trn.models import OrdenBodega
from usr.models import Usuarios

# Create your models here.

class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    estado_id = models.ForeignKey(Estados, on_delete=models.CASCADE, blank=True)
    vista = models.BooleanField(default=False)
    orden = models.ForeignKey(OrdenBodega, on_delete=models.CASCADE, blank=True, null=True)
    orden_prd = models.IntegerField(blank=True, null=True, default=None)
    orden_prv = models.IntegerField(blank=True, null=True, default=None)
    encargado = models.ForeignKey(Usuarios, on_delete=models.CASCADE, blank=True, null=True)
    proveedor_id = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_crea = models.IntegerField(blank=True, null=True)
    