from django.urls import path
from .views import *

urlpatterns = [
    path('notificar/usuarios/', obtener_notificacion, name="obtener_notificacion"),
    path('notificacion/actualizar/', actualizar_notificacion, name="actualizar_notificacion"),

]