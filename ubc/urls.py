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
   path('secciones-bodega/<int:id_bodega>/ajax/', secciones_bodega, name="secciones_bodega"),
   path('modal_editar_pais/<int:id_pais>', modal_editar_pais, name="modal_editar_pais"),
   path('editar_pais/ajax/', editar_pais, name="editar_pais"),
   path('crear_pais_modal/ajax/', modal_crear_pais, name="modal_crear_pais"),
   path('crear_pais/ajax/', crear_pais, name="crear_pais"),
   path('crear_bodega/', crear_bodega, name="crear_bodega"),
   path('detalle-ciudad/<int:id_ciudad>/', detalle_ciudad, name="detalle_ciudad"),
   path('crear_ciudad/', crear_ciudad, name="crear_ciudad"),
]