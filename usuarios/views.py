from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from login.models import Usuarios
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import *


@login_required
@user_passes_test(lambda u: u.id_rol.name != "Panol")
def agregar_usuario(request):
    if request.method == 'POST':
        form = Usarios1(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('usuarios') 
    else:
        form = Usarios1()
    return render(request, 'agregar_usuario.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.id_rol.name != "Panol")
def editar_usuario(request, id):
    usuario = get_object_or_404(Usuarios, id=id)

    if request.method == 'POST':
        form = Usarios1(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = Usarios1(instance=usuario) 

    return render(request, 'agregar_usuario.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.id_rol.name != "Panol")
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuarios, id=id)  
    usuario.delete()  
    return redirect('usuarios')

@login_required
@user_passes_test(lambda u: u.id_rol.name != "Panol")
def index(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'index.html' ,{'Usuarios': usuarios})