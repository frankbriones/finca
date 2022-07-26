from django.urls import path, include

from .views import productos_list, detalle_producto, StockReporte

urlpatterns = [
    path('productos_list/', productos_list, name="productos_list"),
    path('detalles-producto/<int:id_producto>', detalle_producto, name="detalle_producto"),
    path('stock-reporte/',
        StockReporte.as_view(),
        name="stock_reporte"
    ),
]