from django.urls import path, include

from .views import *

urlpatterns = [
    path('list/', stock_bodega, name="stock_bodega"),
]