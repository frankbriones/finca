from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

from bases.views import *

app_name = 'bases'

urlpatterns = [
    path('base/',
        Home.as_view(),
        name="home"
        ),
    path('login/',
        user_login,
        name='login'
        ),
    path('log-out/',
        auth_views.LogoutView.as_view(template_name='bases/login.html'),
        name='log_out'
        ),
    # modal de logout
    path('logout/',
        Logout.as_view(),
        name='logout'
        ),
    path('verificar-correo/',
        verificar_correo,
        name="verificar_correo"),
    path('',
        inicio,
        name="inicio"),
    path('datos_clima/ajax',
        datos_clima,
        name="datos_clima"),
    path('reportes/listado/ajax',
        reportes_list,
        name="reportes_list"),
]