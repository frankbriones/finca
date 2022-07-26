"""finca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('bases.urls', 'bases'), namespace='bases')),
    path('users/', include(('usr.urls', 'usr'), namespace='usr')),
    path('ubicaciones/', include(('ubc.urls', 'ubc'), namespace='ubc')),
    path('personal/', include(('personal.urls', 'personal'), namespace='personal')),
    path('proveedores/', include(('prv.urls', 'prv'), namespace='prv')),
    path('products/', include(('prd.urls', 'prd'), namespace='prd')),
    path('inventario/', include(('inv.urls', 'inv'), namespace='inv')),
    path('transacciones/', include(('trn.urls', 'trn'), namespace='trn')),
    path('notificaciones/', include(('ntf.urls', 'ntf'), namespace='ntf')),
    path('websocket/', include(('wso.urls', 'wso'), namespace='wso')),

    path('password_reset/',
        csrf_exempt(auth_views.PasswordResetView.as_view(
            template_name='bases/contrasena_olvidada.html')
            ), name="password_reset"
        ),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="bases/resetear_contrasena.html"
        ),
        name="password_reset_confirm"
        ),
    path('password_reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
            name="password_reset_done"
        ),
    path('reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='bases/resetear_contrasena_confirmado.html'),
        name="password_reset_complete",
        ),
]

# archivos media en modo debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)
