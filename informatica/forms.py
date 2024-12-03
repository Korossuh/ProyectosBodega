from django import forms
from django.core.exceptions import ValidationError
from .models import *

class DocenteForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Ingrese el nombre','class':'form-control'}
        )
    )
    correo = forms.CharField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Ingrese su Correo','class':'form-control'}
        )
    )
    telefono = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Ingrese su numero','class':'form-control'}
        )
    )
    estado = forms.ChoiceField(
        choices=[
            (1, 'Activo'),
            (0, 'No activo'),
        ],
        widget=forms.RadioSelect(
            attrs={}
        )
    )

    class Meta:
        model = Docente
        fields = ['nombre', 'correo', 'telefono', 'estado']
    
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')

        if Docente.objects.filter(correo=correo).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Debe utilizar otro correo, no se debe repetir")
        return correo

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')

        if Docente.objects.filter(telefono=telefono).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Debe utilizar otro número, no se debe repetir")
        return telefono

class MaterialForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Ingrese el Nombre del Material','class':'form-control'}
        )
    )
    modelo = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Ingrese el Modelo del Material','class':'form-control'}
        )
    )
    stock = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder':'Ingrese el Stock Disponible','class':'form-control'}
        )
    )
    estado = forms.ChoiceField(
        choices=[
            (1,'Activo'),
            (0,'No activo'),
        ],
        widget=forms.RadioSelect
    )

    class Meta:
        model = Material
        fields = ['nombre','modelo','stock','estado']

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        modelo = cleaned_data.get('modelo')

        if nombre and modelo:
            if Material.objects.filter(nombre=nombre, modelo=modelo).exists():
                raise ValidationError("Este material ya existe. Verifica en la Tabla primero")

        return cleaned_data

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = AsignarPrestamo
        fields = ['id_docente', 'id_material', 'cantidad']

    id_docente = forms.ModelChoiceField(
        queryset=Docente.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    id_material = forms.ModelChoiceField(
        queryset=Material.objects.filter(estado=1), 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    cantidad = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese la cantidad', 'class': 'form-control'})
    )

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        material = self.cleaned_data.get('id_material')

        if material:
            material_obj = Material.objects.get(id=material.id)
            if material_obj.stock < cantidad:
                raise ValidationError(f"No hay suficiente stock de {material_obj.nombre}. Solo hay {material_obj.stock} unidades disponibles.")

        return cantidad