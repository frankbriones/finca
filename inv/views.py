from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from prd.models import *

# Create your views here.
@login_required(login_url='/login/')
def stock_bodega(request):
    template_name = 'inv/stock_list.html'
    productos = Productos.objects.all()
    contexto = {
        'inventario': productos
    }
    return render(request, template_name, contexto)