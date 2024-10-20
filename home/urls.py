# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portada, name='portada'),  # Ruta para la portada
]
