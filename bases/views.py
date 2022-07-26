from multiprocessing import AuthenticationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_views

from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required

import json

from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect, JsonResponse

from usr.models import Usuarios
from bases.models import ConfiguracionSistema


# Create your views here.
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base/base.html'
    login_url = 'bases:login'


def user_login(request):
    template_name = 'bases/login.html'
    form = {}
    contexto = {}

    if request.method == 'POST':
        form = AuthenticationForm(request.user, request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # 
        contexto = {'form': form}

        if user:
            if user.estado.descripcion == 'ACTIVO':
                login(request, user)
                return redirect('bases:inicio')
            else:
                contexto = {
                    'mensaje': 'Usuario Inactivo'
                }

    return render(request, template_name, contexto)
         

class Logout(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/logout.html'
    login_url = 'bases:login'


def verificar_correo(request):
    """
    metodo para obtener booleano con existencia del correo
    """
    if request.method == 'GET':
        correo = request.GET['correo']
        if correo:
            usuario = Usuarios.objects.filter(email=correo).first()
            if usuario:
                respuesta = {'existe': True}
            else:
                respuesta = {'existe': False}
            return JsonResponse(respuesta)

@login_required(login_url='/login/')
def inicio(request):
    template_name = 'bases/inicio.html'

    contexto = {}
    return render(request, template_name, contexto)


def datos_clima(request):
    if request.method == 'GET':
        id_ciudad = ConfiguracionSistema.objects.filter(clave='codigo_ciudad').first()
        clave_api = ConfiguracionSistema.objects.filter(clave="key-clima").first()
        string_url = 'https://api.openweathermap.org/data/2.5/weather?id={}&APPID={}&units=metric'.format(id_ciudad.valor, clave_api.valor)
        return JsonResponse({'url': string_url})


def reportes_list(request):
    template_name = 'bases/reportes.html'
    contexto = {

    }
    return render(request, template_name, contexto)