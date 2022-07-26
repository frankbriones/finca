from django.urls import path, include, reverse_lazy

from personal.views import *

app_name = 'personal'

urlpatterns = [
    path('empleados/list/',
        empleados_list,
        name="empleados_list"
        ),
    path('tipo-empleados/list/',
        tipos_empleado_list,
        name="tipos_list"
        ),
    path('categorias-empleados/list/',
        categorias_empleado_list,
        name="categorias_list"
        ),
    # ajax
    path('categorias-empleados/list/ajax',
        categorias_ajax,
        name="categorias_ajax"
        ),
    
    path('lista-empleados/ajax',
        listado_empleados_ajax,
        name="listado_empleados_ajax"
        ),
    path('actualizar-categoria/personal/<int:id_categoria>',
        actualizar_categoria_personal,
        name="actualizar_categoria_personal"
        ),
    path('editar-categoria/', editar_categoria, name="editar_categoria")
]