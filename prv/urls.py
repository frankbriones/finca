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
        ProveedoresReporte.as_view(),
        name="proveedores_reporte"
    ),
]