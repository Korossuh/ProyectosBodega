from django.contrib.auth.models import AbstractUser
from django.db import models

class Rol(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Usuarios(AbstractUser):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=1000)
    created = models.DateField(verbose_name="Fecha de Creacion: ", auto_now=True)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True, blank=True )
    update = models.DateField(verbose_name="Ultima Modificacion: ", auto_now= True)
    estado = models.IntegerField(verbose_name="estado", null=True, blank=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="usuarios_groups",  # Cambia el related_name porque si no tira tremendo hate
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="usuarios_permissions",  # Cambia el related_name porque si no esto tira tremendo hate
        blank=True,
    )

class Docente(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length = 50)
    telefono = models.IntegerField(verbose_name="Numero de Telefono")
    created = models.DateField(verbose_name="Fecha de Creacion: ", auto_now=True)
    update = models.DateField(verbose_name="Ultima Modificacion:", auto_now=True)
    estado = models.IntegerField(verbose_name="estado")

class Materiales(models.Model):
    Nombre = models.CharField(max_length=50)
    Modelo = models.CharField(max_length=50)
    Stock = models.IntegerField(verbose_name="Stock")
    estado = models.IntegerField(verbose_name="Estado")
    def __str__(self):
        return self.Nombre

class Asignacion_Materiales(models.Model):
    id_docente = models.ForeignKey(Docente, verbose_name="Id del Profesor", on_delete=models.CASCADE)
    id_material = models.ForeignKey(Materiales, verbose_name="ID del Material", on_delete=models.CASCADE)
    Cantidad = models.IntegerField(max_length=1000)
    estado = models.IntegerField()

# Create your models here.
