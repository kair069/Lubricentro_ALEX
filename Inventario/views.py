from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Producto, Marca, Categoria
from .forms import ProductoForm

from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ProductoForm
from .models import Producto, Marca, Categoria

from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ProductoForm
from .models import Producto, Marca, Categoria

def lista_productos(request):
    # Manejar el formulario de creación de productos
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()

    # Obtener la consulta de búsqueda y filtros
    query = request.GET.get('q', '')  # Consulta de búsqueda de texto
    marca_id = request.GET.get('marca', '')  # Filtro por marca
    categoria_id = request.GET.get('categoria', '')  # Filtro por categoría
    sae = request.GET.get('sae', '')  # Filtro por SAE
    precio_min = request.GET.get('precio_min', '')  # Filtro por rango de precio mínimo
    precio_max = request.GET.get('precio_max', '')  # Filtro por rango de precio máximo

    # Filtro base para productos
    productos = Producto.objects.all()

    # Aplicar filtro de búsqueda de texto
    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) |
            Q(marca__nombre__icontains=query) |
            Q(categoria__nombre__icontains=query)
        )

    # Aplicar filtro de marca
    if marca_id:
        productos = productos.filter(marca_id=marca_id)

    # Aplicar filtro de categoría
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    # Aplicar filtro de SAE
    if sae:
        productos = productos.filter(sae__icontains=sae)

    # Aplicar filtro de rango de precios
    if precio_min:
        productos = productos.filter(precio_venta__gte=precio_min)
    if precio_max:
        productos = productos.filter(precio_venta__lte=precio_max)

    # Obtener todas las marcas y categorías disponibles
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()

    # Obtener el historial de productos vistos desde la sesión
    productos_vistos_ids = request.session.get('productos_vistos', [])
    productos_vistos = Producto.objects.filter(id__in=productos_vistos_ids)

    # Paginar los productos
    paginator = Paginator(productos, 10)  # Mostrar 10 productos por página
    page_number = request.GET.get('page')  # Obtener el número de página de la URL
    page_obj = paginator.get_page(page_number)  # Obtener los productos para esa página
    
    context = {
        'form': form,
        'productos': page_obj,  # Usar los productos paginados
        'query': query,
        'marcas': marcas,
        'categorias': categorias,
        'marca_id': marca_id,
        'categoria_id': categoria_id,
        'sae': sae,
        'precio_min': precio_min,
        'precio_max': precio_max,
        'productos_vistos': productos_vistos,
        'page_obj': page_obj,  # Pasar el objeto de paginación al contexto
    }

    return render(request, 'productos/lista_productos.html', context)
        



def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    # Agregar el producto a la lista de productos vistos
    if 'productos_vistos' not in request.session:
        request.session['productos_vistos'] = []
    
    productos_vistos = request.session['productos_vistos']

    if producto.id not in productos_vistos:
        productos_vistos.append(producto.id)
        request.session['productos_vistos'] = productos_vistos

    context = {
        'producto': producto,
    }
    
    return render(request, 'productos/detalle_producto.html', context)

from django.contrib import messages
# def crear_producto(request):
#     if request.method == 'POST':
#         form = ProductoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Producto creado exitosamente.')  # Mensaje de éxito
#             return redirect('lista_productos')  # Redirige a la lista de productos después de guardar
#         else:
#             messages.error(request, 'Error al crear el producto. Verifica los datos ingresados.')  # Mensaje de error
#     else:
#         form = ProductoForm()

#     context = {
#         'form': form,
#     }
    
#     return render(request, 'productos/crear_producto.html', context)
###################################  crear producto
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductosForms

from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def crear_producto(request):
    if request.method == 'POST':
        form = ProductosForms(request.POST, request.FILES)  # Soporte para archivos
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente.')  # Mensaje de éxito
            return redirect('lista_productos')  # Redirige a la lista de productos después de guardar
        else:
            messages.error(request, 'Error al crear el producto. Verifica los datos ingresados.')  # Mensaje de error
    else:
        form = ProductosForms()

    context = {
        'form': form,
    }
    
    return render(request, 'productos/crear_producto.html', context)




def crear_marca(request):
    if request.method == 'POST':
        nombre_marca = request.POST.get('nombre_marca')
        # Crear y guardar la marca aquí...
        nueva_marca = Marca.objects.create(nombre=nombre_marca)
        return JsonResponse({'id': nueva_marca.id, 'nombre': nueva_marca.nombre})

def crear_categoria(request):
    if request.method == 'POST':
        nombre_categoria = request.POST.get('nombre_categoria')
        nueva_categoria = Categoria.objects.create(nombre=nombre_categoria)
        return JsonResponse({'id': nueva_categoria.id, 'nombre': nueva_categoria.nombre})

####################################


from django.shortcuts import get_object_or_404, redirect, render
from .models import Producto
from .forms import ProductoForm

def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)

    context = {
        'form': form,
        'producto': producto,
    }

    return render(request, 'productos/actualizar_producto.html', context)



from django.contrib import messages

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('lista_productos')

    return render(request, 'productos/eliminar_producto.html', {'producto': producto})

# inventario/views.py
    
# inventario/views.py
import pandas as pd
from django.shortcuts import render
from .models import Producto, Marca, Categoria

def cargar_datos_excel(request):
    # Ruta del archivo Excel
    ruta_excel = r"C:\Users\Acer\Desktop\DATOS_NUEVO.xlsx"
    
    # Leer el archivo Excel (hoja llamada 'INVENTARIO')
    df = pd.read_excel(ruta_excel, sheet_name='INVENTARIO')

    # Reemplazar NaN por un valor adecuado (por ejemplo, 0 o None según el contexto)
    df = df.fillna({
        'Cantidad': 0,
        'Precio_Venta': 0.0,
        'Stock': 0,
        'Precio_Costo': 0.0,
        'Tipo de motor': '',
        'Sae': '',
        'Tipo de filtro': '',
        'Tipo de Envase': '',
        'DESCRIPCION': '',
    })

    # Iterar sobre las filas del DataFrame y crear instancias de Producto
    for index, row in df.iterrows():
        # Obtener o crear la marca y la categoría
        marca_obj, _ = Marca.objects.get_or_create(nombre=row['Marca'])
        categoria_obj, _ = Categoria.objects.get_or_create(nombre=row['Categoría'])

        # Crear el producto
        producto = Producto(
            nombre=row['Nombre del producto'],
            marca=marca_obj,
            categoria=categoria_obj,
            tipo_motor=row['Tipo de motor'] if row['Tipo de motor'] != '' else None,
            sae=row['Sae'] if row['Sae'] != '' else None,
            tipo_filtro=row['Tipo de filtro'] if row['Tipo de filtro'] != '' else None,
            imagen_url=row['Imagen URL'] if row['Imagen URL'] != '' else None,
            cantidad=row['Cantidad'],
            precio_venta=row['Precio_Venta'],
            stock=row['Stock'],
            tipo_envase=row['Tipo de Envase'] if row['Tipo de Envase'] != '' else None,
            precio_costo=row['Precio_Costo'] if row['Precio_Costo'] != 0.0 else None,
            descripcion=row['DESCRIPCION'] if row['DESCRIPCION'] != '' else None
        )

        # Guardar el producto en la base de datos
        producto.save()

    return render(request, 'productos/carga_exitosa.html')



from django.shortcuts import render
from .forms import CalcularCostoForm
from .models import Producto

from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto
from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto
from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto
from decimal import Decimal

def calcular_costo(request):
    productos = Producto.objects.all()
    query = request.GET.get('q', '')

    if query:
        productos = productos.filter(nombre__icontains=query)

    if request.method == 'POST':
        producto_ids = request.POST.getlist('producto_ids')
        cantidades = request.POST.getlist('cantidades')

        total_costo = Decimal(0)

        # Asegurarse de que la longitud de producto_ids y cantidades sea la misma
        if len(producto_ids) != len(cantidades):
            messages.error(request, 'El número de productos y cantidades no coincide.')
            return redirect('calcular_costo')

        for producto_id, cantidad in zip(producto_ids, cantidades):
            # Verificar que la cantidad sea un número entero
            try:
                cantidad = int(cantidad)
                if cantidad < 1:
                    raise ValueError("La cantidad debe ser al menos 1.")
            except ValueError:
                messages.error(request, f'Cantidad inválida para el producto con ID {producto_id}.')
                return redirect('calcular_costo')

            producto = get_object_or_404(Producto, pk=producto_id)
            costo = Decimal(producto.precio_venta) * cantidad
            total_costo += costo

        resultado = total_costo / Decimal(1.18)

        messages.success(request, f'El costo total calculado es: {resultado:.2f}')
        return redirect('calcular_costo')

    context = {
        'productos': productos,
        'query': query,
    }
    
    return render(request, 'productos/calcular_costo.html', context)




from django.shortcuts import render
from .models import Producto

def analisis_costos(request):
    productos = Producto.objects.all()
    
    # Cálculos
    total_costos = sum(producto.precio_costo * producto.stock for producto in productos if producto.precio_costo is not None)
    total_ventas = sum(producto.precio_venta * producto.stock for producto in productos)
    margen_ganancia = total_ventas - total_costos if total_costos else 0

    context = {
        'total_costos': total_costos,
        'total_ventas': total_ventas,
        'margen_ganancia': margen_ganancia,
        'productos': productos,
    }

    return render(request, 'estadisticas/analisis_costos.html', context)


from django.shortcuts import render
from .models import Producto

def estadisticas_inventario(request):
    # Consultar todos los productos
    productos = Producto.objects.all()
    
    precio_venta_total = 0
    stock_total = 0
    inversion_total = 0
    costo_total = 0

    # Calcular los KPIs
    for producto in productos:
        # Calcular precio de venta total
        precio_venta_total += producto.precio_venta * producto.stock
        
        # Sumar stock total
        stock_total += producto.stock
        
        # Verificar si precio_costo es None antes de usarlo
        if producto.precio_costo is not None:
            inversion_total += producto.precio_costo * producto.stock
            # Sumar costo total solo para productos de aceite de motor
            if 'Aceite de Motor' in producto.nombre:
                costo_total += producto.precio_costo * producto.stock

    # Calcular precio de venta por stock
    precio_venta_por_stock = precio_venta_total / stock_total if stock_total > 0 else 0

    context = {
        'precio_venta_total': precio_venta_total,
        'stock_total': stock_total,
        'precio_venta_por_stock': precio_venta_por_stock,
        'inversion_total': inversion_total,
        'costo_total': costo_total,
    }

    return render(request, 'estadisticas/estadisticas.html', context)



###########################GRAFICAS

import io
import base64
from django.shortcuts import render
from django.db.models import Sum
from .models import Producto
import matplotlib.pyplot as plt
import pandas as pd

def ventas_por_marca_view(request):
    # Generar los datos para la gráfica de ventas por marca
    ventas = Producto.objects.values('marca__nombre').annotate(total_ventas=Sum('precio_venta'))
    labels = [venta['marca__nombre'] for venta in ventas]
    sizes = [venta['total_ventas'] for venta in ventas]

    # Crear la gráfica
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Gráfica en forma de círculo

    # Guardar la imagen en un objeto bytes
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()  # Cerrar la figura para liberar memoria

    return render(request, 'estadisticas/estadisticas.html', {'img_str': img_str})

# def categoria_distribution_view(request):
#     # Generar los datos para la gráfica de distribución de productos por categoría
#     categorias = Producto.objects.values('categoria__nombre').annotate(num_productos=Sum('id'))
#     labels, values = zip(*[(cat['categoria__nombre'], cat['num_productos']) for cat in categorias])

#     # Crear la gráfica
#     plt.figure(figsize=(10, 6))
#     plt.bar(labels, values)
#     plt.xlabel('Categorías')
#     plt.ylabel('Número de Productos')
#     plt.title('Distribución de Productos por Categoría')
#     plt.xticks(rotation=45)

#     # Guardar la imagen en un objeto bytes
#     buffer = io.BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     img_str_categoria = base64.b64encode(buffer.getvalue()).decode('utf-8')
#     plt.close()  # Cerrar la figura para liberar memoria

#     return render(request, 'estadisticas/estadisticas.html', {'img_str_categoria': img_str_categoria})

# def stock_trend_view(request):
#     # Generar los datos para la gráfica de tendencia de stock de productos
#     productos = Producto.objects.values('nombre', 'fecha_actualizacion', 'stock')
#     df = pd.DataFrame(list(productos))

#     # Agrupar los datos por fecha
#     df_grouped = df.groupby('fecha_actualizacion').sum()['stock']

#     # Crear la gráfica
#     plt.figure(figsize=(10, 6))
#     df_grouped.plot(kind='line')
#     plt.title('Tendencia de Stock de Productos')
#     plt.xlabel('Fecha')
#     plt.ylabel('Stock')
#     plt.xticks(rotation=45)

#     # Guardar la imagen en un objeto bytes
#     buffer = io.BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     img_str_stock = base64.b64encode(buffer.getvalue()).decode('utf-8')
#     plt.close()  # Cerrar la figura para liberar memoria

#     return render(request, 'estadisticas/estadisticas.html', {'img_str_stock': img_str_stock})
