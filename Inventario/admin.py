from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Producto

# @admin.register(Producto)
# class ProductoAdmin(admin.ModelAdmin):
#     list_display = ('nombre', 'marca', 'categoria', 'precio_venta', 'stock')
#     search_fields = ('nombre', 'marca', 'categoria')