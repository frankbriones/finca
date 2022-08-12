from django.urls import path, include

from .views import productos_list, detalle_producto, StockReporte, secciones_bodega, validar_cantidad_produccion,\
    categorias_insumos_list, actualizar_categoria_insumo, editar_categoria, unidades_medidas_list,\
    actualizar_unidad_medida, editar_unidad_medida

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
    path('insumos-categorias/list/',
        categorias_insumos_list,
        name="categorias_insumos_list"
    ),
    path('actualizar_categoria_insumos/<int:id_categoria>',
        actualizar_categoria_insumo,
        name="actualizar_categoria_insumo"
    ),
    path('editar-categoria_insumo/',
        editar_categoria,
        name="editar_categoria"
    ),
    path('unidades-medida/list/',
        unidades_medidas_list,
        name="unidades_medidas_list"
    ),
    path('actualizar_unidad_medida/<int:id_categoria>',
        actualizar_unidad_medida,
        name="actualizar_unidad_medida"
    ),
    path('editar-unida-medida/',
        editar_unidad_medida,
        name="editar_unidad_medida"
    ),

]