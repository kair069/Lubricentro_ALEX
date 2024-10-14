# clientes/models.py
from django.db import models
from Inventario.models import Producto  # Importa el modelo Producto desde el app 'productos'

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='clientes/', blank=True, null=True)
    dni = models.CharField(max_length=20, unique=True)

    def clean(self):
        # Validación del teléfono
        if self.telefono and not self.telefono.isdigit():
            raise ValidationError('El teléfono debe contener solo dígitos.')

        # Validación del DNI
        if not self.dni.isalnum() or len(self.dni) < 8:
            raise ValidationError('El DNI debe contener al menos 8 caracteres alfanuméricos.')

        # Validación de la imagen
        if self.imagen:
            file_extension = self.imagen.name.split('.')[-1].lower()
            valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
            if file_extension not in valid_extensions:
                raise ValidationError('La imagen debe ser de tipo JPG, JPEG, PNG o GIF.')



    

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre} comprados por {self.cliente.nombre}"

