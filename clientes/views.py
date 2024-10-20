from django.shortcuts import get_object_or_404, render

# Create your views here.
# clientes/views.py
from django.shortcuts import render, redirect
from django.views import View
from .models import Cliente
from .forms import ClienteForm

class ClienteListView(View):
    def get(self, request):
        clientes = Cliente.objects.all()  # Obtiene todos los clientes
        return render(request, 'clientes/cliente_list.html', {'clientes': clientes})




from django.contrib import messages

# 2. Crear un nuevo cliente (Create)
class ClienteCreateView(View):
    def get(self, request):
        form = ClienteForm()
        return render(request, 'clientes/cliente_form.html', {'form': form})

    def post(self, request):
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente agregado exitosamente.')
            return redirect('cliente_list')
        messages.error(request, 'Error al agregar el cliente. Verifique los datos.')
        return render(request, 'clientes/cliente_form.html', {'form': form})

# 3. Editar un cliente existente (Update)
class ClienteUpdateView(View):
    def get(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        form = ClienteForm(instance=cliente)
        return render(request, 'clientes/cliente_form.html', {'form': form})

    def post(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado exitosamente.')
            return redirect('cliente_list')
        messages.error(request, 'Error al actualizar el cliente.')
        return render(request, 'clientes/cliente_form.html', {'form': form})

# 4. Eliminar un cliente (Delete)
class ClienteDeleteView(View):
    def get(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        return render(request, 'clientes/cliente_confirm_delete.html', {'cliente': cliente})

    def post(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        cliente.delete()
        messages.success(request, 'Cliente eliminado exitosamente.')
        return redirect('cliente_list')
