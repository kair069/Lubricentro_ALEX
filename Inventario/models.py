from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tipo_motor = models.CharField(max_length=100, blank=True, null=True)
    sae = models.CharField(max_length=20, blank=True, null=True)
    tipo_filtro = models.CharField(max_length=100, blank=True, null=True)
    imagen_url = models.URLField(max_length=500, blank=True, null=True)
    cantidad = models.PositiveIntegerField(default=0)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    tipo_envase = models.CharField(max_length=100, blank=True, null=True)
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)  # Campo de fecha de actualización automática

    def __str__(self):
        return self.nombre


