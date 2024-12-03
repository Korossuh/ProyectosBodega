from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuarios, Rol
from .forms import Creacion_Usuario, Editar_Usuario

class CustomUserAdmin(UserAdmin):
    add_form = Creacion_Usuario
    form = Editar_Usuario
    model = Usuarios
    list_display = ("username", "nombre", "correo", "id_rol", "estado", "is_active", "is_staff")
    list_filter = ("id_rol", "estado", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Información Personal", {"fields": ("nombre", "correo", "id_rol", "estado")}),
        ("Permisos", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "nombre", "correo", "password1", "password2", "id_rol", "estado", "is_active", "is_staff"),
        }),
    )
    search_fields = ("username", "nombre", "correo")
    ordering = ("username",)

admin.site.register(Usuarios, CustomUserAdmin)
admin.site.register(Rol)

# Register your models here.
