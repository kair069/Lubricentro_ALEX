# clientes/urls.py
from django.urls import path
from .views import ClienteDeleteView, ClienteListView, ClienteCreateView, ClienteUpdateView

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente_list'),  # Vista para listar clientes
    path('nuevo/', ClienteCreateView.as_view(), name='cliente_create'),  # Vista para crear nuevo cliente
    path('<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente_delete'),
]
