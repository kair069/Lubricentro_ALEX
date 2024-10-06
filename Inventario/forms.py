# mi_aplicacion/forms.py

from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'marca',
            'categoria',
            'tipo_motor',
            'sae',
            'tipo_filtro',
            'imagen_url',
            'cantidad',
            'precio_venta',
            'stock',
            'tipo_envase',
            'precio_costo',
            'descripcion',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'tipo_motor': forms.TextInput(attrs={'class': 'form-control'}),
            'sae': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_filtro': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen_url': forms.URLInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_envase': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class CalcularCostoForm(forms.Form):
    productos = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    
    
    
from django import forms
from .models import Producto
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProductosForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar Producto'))

class ProductonFormn(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre', 'marca', 'categoria', 'tipo_motor', 'sae',
            'tipo_filtro', 'imagen_url',  # Cambiar 'imagen' por 'imagen_url'
            'cantidad', 'precio_venta', 'stock', 
            'tipo_envase', 'precio_costo', 'descripcion'
        ]
