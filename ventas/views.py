from pyexpat.errors import messages
from django.shortcuts import render

# Create your views here.
# ventas/views.py
from django.shortcuts import render, redirect

from clientes.models import Cliente
from .forms import VentaForm

# ventas/views.py
from django.shortcuts import render, redirect
from .forms import VentaForm
from .models import Venta,Producto

def agregar_venta(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    clientes = Cliente.objects.all()  # Obtener todos los clientes

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')  # Obtener el ID del cliente seleccionado
        cantidades = {key: int(value) for key, value in request.POST.items() if key.startswith('cantidad_')}
        
        # Validar que al menos un producto haya sido seleccionado
        if not cantidades:
            messages.error(request, 'Debes seleccionar al menos un producto para la venta.')
            return redirect('agregar_venta')  # Redirigir si no hay productos seleccionados

        for producto_id, cantidad in cantidades.items():
            producto = Producto.objects.get(id=producto_id.split('_')[1])  # Extraer el ID del producto
            # Crear una nueva venta
            venta = Venta(
                cliente_id=cliente_id,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=producto.precio_venta  # Suponiendo que tienes un campo de precio en Producto
            )
            venta.save()  # Guardar la venta

        messages.success(request, 'Venta registrada exitosamente.')  # Aquí es donde se agrega el mensaje
        return redirect('venta_lista')  # Redirigir a la lista de ventas

    return render(request, 'ventas/agregar_venta.html', {
        'productos': productos,
        'clientes': clientes,
    })

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})
