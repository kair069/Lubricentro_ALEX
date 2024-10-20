# ventas/forms.py
from django import forms
from .models import Venta
from Inventario.models import Producto

from django import forms
from .models import Producto

class VentaForm(forms.Form):
    cliente = forms.CharField(max_length=200)  # Cambia esto si tienes un modelo de cliente
    productos = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
