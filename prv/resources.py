from datetime import datetime
import pytz

from django.db.models import Count, Max, Min, Sum, F, Q, When, Subquery


from import_export import resources
from import_export.fields import Field
from prv.models import Proveedores

class ProveedoresResource(resources.ModelResource):
    fecha_creacion = Field(
        attribute='fecha_creacion',
        column_name='Fecha Creacion'
    )

    nombres = Field(
        attribute='nombres',
        column_name="Nombres"
    )
    apellidos = Field(
        attribute='apellidos',
        column_name="Apellidos"
    )
    direccion = Field(
        attribute='direccion',
        column_name="Direccion"
    )

    telefono = Field(
        attribute='telefono',
        column_name="Telefono"
    )

    correo = Field(
        attribute='correo',
        column_name="Email"
    )

    ciudad = Field(
        attribute='ciudad',
        column_name="Ciudad"
    )

    usuario = Field(
        attribute='usuario',
        column_name="USERNAME"
    )

    class Meta:
        model = Proveedores
        fields = (
            'fecha_creacion', 'nombres', 'apellidos', 'direccion', 'telefono',
            'correo', 'ciudad', 'usuario'
        )

    def dehydrate_fecha_creacion(self, Proveedores):  
        formato_fecha = "%d/%m/%Y - %H:%M:%S"
        registro = (Proveedores.fecha_creacion)
        if registro is not None:
            registro = cambiar_zona('America/Guayaquil', registro)
            fecha_creacion = datetime.strftime(registro, formato_fecha)
        else:
            fecha_creacion = "No tenemos registro."
        
        return fecha_creacion



def cambiar_zona(zona_horaria, registro):
    zona_horaria = pytz.timezone(zona_horaria)
    registro = registro.replace(tzinfo=zona_horaria)
    return registro