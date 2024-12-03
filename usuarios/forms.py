from django import forms
from login.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
estado = (
    ("0", "Inactivo"),
    ("1", "Activo")
)

class Usarios1(forms.ModelForm):
    id_rol = forms.ModelChoiceField(queryset=Rol.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control'}), label='Rol')
    estado = forms.ChoiceField(choices=estado, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Usuarios
        fields = ['nombre', 'correo', 'password', 'id_rol', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electronico'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
            'estado': forms.Select(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        usuario = super().save(commit=False)
        
        usuario.username = usuario.nombre
        usuario.set_password(self.cleaned_data['password'])
        usuario.is_active = usuario.estado

        if commit:
            usuario.save()
        
        return usuario