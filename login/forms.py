from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Usuarios

class Creacion_Usuario(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = (
            "username",
            "nombre",
            "correo",
            "password",
            "id_rol",
            "estado",
        )
        widgets = {
            "password": forms.PasswordInput(),
            "estado": forms.NumberInput(attrs={"no activo": 0, "activo": 1}),
        }

class Editar_Usuario(UserChangeForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'correo', 'password', 'id_rol', 'estado']

class FormularioLogin(AuthenticationForm):
    username = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña",
    widget=forms.PasswordInput(attrs={'class': 'form-control'}))