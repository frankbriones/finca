from django.urls import path, include, reverse_lazy

from ubc.views import *

app_name = 'ubc'

urlpatterns = [
   path('list/pais', pais_list, name="pais_list"),
   path('list/ciudades/', ciudad_list, name="ciudad_list"),
   path('list/sectores/', sectores_list, name="sectores_list"),
   path('list/lotes/', lotes_list, name="lotes_list"),
   path('list/bodegas/', bodegas_list, name="bodegas_list"),
   path('actualizar-pais/<int:id_pais>/', actualizar_pais, name="actualizar_pais"),
   path('actualizar-ciudad/<int:id_ciudad>/', actualizar_ciudad, name="actualizar_ciudad"),
   path('actualizar-sector/<int:id_sector>/', actualizar_sector, name="actualizar_sector"),
   path('actualizar-lote/<int:id_lote>/', actualizar_lote, name="actualizar_lote"),
   path('detalle-bodega/<int:id_bodega>/', detalle_bodega, name="detalle_bodega"),
   path('editar-bodega/<int:id_bodega>/', editar_bodega, name="editar_bodega"),
   path('secciones-bodega/<int:id_bodega>/ajax/', secciones_bodega, name="secciones_bodega")

]