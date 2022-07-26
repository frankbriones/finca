from datetime import datetime
import pytz

from django.db.models import Count, Max, Min, Sum, F, Q, When, Subquery


from import_export import resources
from import_export.fields import Field
from prd.models import Productos

class ProductoResource(resources.ModelResource):

    fecha_creacion = Field(
        attribute='fecha_creacion',
        column_name='Fecha Creacion'
    )
    descripcion = Field(
        attribute='descripcion',
        column_name='Descripcion'
    )
    categoria = Field(
        attribute='categoria',
        column_name='Categoria'
    )
    estado = Field(
        attribute='estado',
        column_name='Estado'
    )

    unidad_medida = Field(
        attribute='unidad_medida',
        column_name='Unidad Medida'
    )

    cantidad_minima = Field(
        attribute='cantidad_minima',
        column_name='Cantidad Minima'
    )

    cantidad_existente = Field(
        attribute='cantidad_existente',
        column_name='Existencia'
    )

    bodega = Field(
        attribute='bodega',
        column_name='Bodega'
    )

    class Meta:
        model = Productos
        fields = (
            'fecha_creacion', 'descripcion', 'categoria', 'estado', 'unidad_medida',
            'cantidad_minima', 'cantidad_existente', 'bodega'
        )


    def dehydrate_fecha_creacion(self, Productos):  
        formato_fecha = "%d/%m/%Y - %H:%M:%S"
        registro = (Productos.fecha_creacion)
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