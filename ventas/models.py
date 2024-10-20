from django.db import models

# Create your models here.
# ventas/models.py
from django.db import models
from clientes.models import Cliente  # Asegúrate de que el modelo Cliente exista
from Inventario.models import Producto  # Asegúrate de que el modelo Producto exista

# ventas/models.py
from django.db import models
from Inventario.models import Producto  # Asegúrate de importar tu modelo de Producto

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)  # Añadido
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)  # Añadido
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calcula el total de la venta
        self.total_venta = self.precio_unitario * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre} vendidos"
