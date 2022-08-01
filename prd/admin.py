from django.contrib import admin

# Register your models here.

from .models import *

#admin.site.register(Productos)
admin.site.register(CategoriaProducto)
admin.site.register(UnidadMedida)