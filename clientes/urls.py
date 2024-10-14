# clientes/urls.py
from django.urls import path
from .views import ClienteListView, ClienteCreateView

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente_list'),  # Vista para listar clientes
    path('nuevo/', ClienteCreateView.as_view(), name='cliente_create'),  # Vista para crear nuevo cliente
]
