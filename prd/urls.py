from django.urls import path, include

from .views import productos_list, detalle_producto, StockReporte, secciones_bodega, validar_cantidad_produccion

urlpatterns = [
    path('productos_list/', productos_list, name="productos_list"),
    path('detalles-producto/<int:id_producto>', detalle_producto, name="detalle_producto"),
    path('stock-reporte/',
        StockReporte.as_view(),
        name="stock_reporte"
    ),
    path('secciones-bodega/',
        secciones_bodega,
        name="secciones_bodega"
    ),
    path('insumos/validar_cantidad_produccion/ajax',
        validar_cantidad_produccion,
        name="validar_cantidad_produccion"
    ),
]