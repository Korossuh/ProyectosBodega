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
    created = models.DateField(auto_now=True)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True, blank=True )
    update = models.DateField(auto_now= True)
    estado = models.IntegerField(null=True, blank=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="usuarios_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="usuarios_permissions",
        blank=True,
    )

