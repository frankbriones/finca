from django.urls import path, include, reverse_lazy
from .views import *
from prv.views import proveedores_ajax
app_name="trn"

urlpatterns = [
    path('pedidos-list/', pedidos_list, name="pedidos_list"),
    path('ingresos-list/', ingresos_list, name="ingresos_list"),
    path('orden-produccion-list/', orden_produccion_list, name="orden_produccion_list"),
    path('crear-solicitud/', crear_pedido, name="crear_pedido"),
    path('detalle-pedido/<int:id_solicitud>', detalle_solicitud, name="detalle_solicitud"),
    path('detalle-pedido/<int:id_solicitud>', informacion_pedido, name="informacion_pedido"),
    path('solicitud/<int:id_solicitud>',
        solicitud_modal,
        name="solicitud_modal"
    ),
    path('generar-ingreso/bodega/<int:id_solicitud>', generar_orden, name="generar_orden"),
    path('actualiza-stock/<int:id_orden>', actualiza_stock, name="actualiza_stock"),
    path('proveedores-pedidos/list/ajax',
        proveedores_ajax,
        name="proveedores_ajax"
    ),
    path('listado-pedidos/ajax/', listado_pedidos_ajax, name="listado_pedidos_ajax"),
    path('enviar_orden/<int:id_solicitud>/ajax/', enviar_orden, name="enviar_orden"),
    path('recibir_pedido/<int:id_solicitud>/', recibir_pedido, name="recibir_pedido"),
    path('despachar_pedido/<int:id_solicitud>/', despachar_pedido, name="despachar_pedido"),
    path('generar_orden_ingreso/bodeguero/', generar_orden_ingreso, name="generar_orden_ingreso"),


    path('generar_documento/<int:id_solicitud>/', generar_documento, name="generar_documento"),
    path('detalle-orden/produccion/<int:id_orden>', orden_produccion_modal, name="orden_produccion_modal"),
    path('lista-productos/ajax/', lista_productos_ajax, name="lista_productos_ajax"),
    path('crear-orden/produccion/ajax/', orden_produccion_crear, name="orden_produccion_crear"),
    path('detalle/produccion/<int:id_orden>', detalle_orden_produccion, name="detalle_orden_produccion"),

    path('lista-ordenes/salida/', ordenes_salida_list, name="ordenes_salida_list"),
    path('procesar-orden/<int:id_orden>', procesar_orden, name="procesar_orden"),
    path('generar_orden_salida/bodega/<int:id_orden>', generar_orden_salida, name="generar_orden_salida"),
    path('orden_salida/bodega/', generar_orden_salida_bodega, name="generar_orden_salida_bodega"),

    path('actualiza-stock/salida/<int:id_orden>', actualiza_stock_salida, name="actualiza_stock_salida"),

    path('actualizar_orden_bodega/recibida/<int:id_orden>/', marcar_orden_revisada, name="marcar_orden_revisada"),

    path('actualizar_orden_produccion/recibida/<int:id_orden>/', revisar_orden_produccion, name="revisar_orden_produccion"),

    path('detalle_orden/ingreso/<int:id_orden>/', orden_ingreso_detalle, name="orden_ingreso_detalle"),
    path('detalle_orden/salida/<int:id_orden>/', orden_salida_detalle, name="orden_salida_detalle"),
    path('lista_categorias_productos_ajax/', lista_categorias_productos, name="lista_categorias_productos_ajax"),
    path('eliminar_insumo_solic_produccion/ajax/', eliminar_insumo_solic_produccion, name="eliminar_insumo_solic_produccion"),
    path('eliminar_solicitud_prod/ajax/', eliminar_solicitud_prod, name="eliminar_solicitud_prod"),

]