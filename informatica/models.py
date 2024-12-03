from django.db import models

# Modelo para docentes
class Docente(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50, unique=True)
    telefono = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    estado = models.IntegerField()

    def __str__(self):
        return self.nombre

# Modelo para materiales
class Material(models.Model):
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    stock = models.IntegerField()
    estado = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.modelo})"

class AsignarPrestamo(models.Model):
    id_docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    id_material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    estado = models.IntegerField(default=1)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Préstamo: {self.id_material.nombre} a {self.id_docente.nombre} (Cantidad: {self.cantidad})"