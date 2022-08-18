from django.urls import path, include

from .views import *

urlpatterns = [
    path('list/', proveedores_list, name="proveedores_list"),
    path('actualizar-proveedor/<int:id_proveedor>',
        actualizar_proveedor_personal,
        name="actualizar_proveedor_personal"
    ),
    path('editar-proveedor/<int:id_proveedor>',
        editar_proveedor_modal,
        name="editar_proveedor_modal"
    ),
    path('proveedores-reporte/',
        ProveedoresReporte,
        name="proveedores_reporte"
    ),
    path('proveedores-categorias/list/',
        categorias_prov_list,
        name="categorias_prov_list"
    ),
    path('actualizar_categoria_proveedor/<int:id_categoria>',
        actualizar_categoria_proveedor,
        name="actualizar_categoria_proveedor"
    ),
    path('editar-categoria_proveedor/',
        editar_categoria,
        name="editar_categoria"
    ),

]