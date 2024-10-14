from django.shortcuts import render

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

class ClienteCreateView(View):
    def get(self, request):
        form = ClienteForm()
        return render(request, 'clientes/cliente_form.html', {'form': form})

    def post(self, request):
        form = ClienteForm(request.POST, request.FILES)  # Incluye archivos (imagen)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')  # Redirige a la lista de clientes
        return render(request, 'clientes/cliente_form.html', {'form': form})
