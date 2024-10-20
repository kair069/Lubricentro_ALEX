# ventas/urls.py
from django.urls import path
from .views import agregar_venta, lista_ventas

urlpatterns = [
    path('agregar/', agregar_venta, name='agregar_venta'),
    path('lista/', lista_ventas, name='venta_lista'),
    # Aquí puedes agregar más URLs para listar ventas, etc.
]
