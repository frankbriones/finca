from django.shortcuts import render

from prd.models import *

# Create your views here.
def stock_bodega(request):
    template_name = 'inv/stock_list.html'
    productos = Productos.objects.all()
    contexto = {
        'inventario': productos
    }
    return render(request, template_name, contexto)