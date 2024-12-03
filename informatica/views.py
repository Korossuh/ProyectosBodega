from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def inicio(request):
    if request.user.id_rol:
        role_name = request.user.id_rol.name
        if role_name == "Panol":
            return redirect("indexpanol")  
        elif role_name == "Administrador":
            return redirect("index")  
    return redirect("index") 

@login_required
@user_passes_test(lambda u: u.id_rol.name != "Panol")
def index(request):
    return render(request, "inicio/index.html")

@login_required
@user_passes_test(lambda u: u.id_rol.name != "Administrador")
def panol(request):
    return render(request,"inicio/panol.html")

#
# Views para CRUDS de Administrador
#

#CRUD Docente
@login_required
@user_passes_test(lambda u: u.id_rol.name != "Panol")
def docente(request):
    docentes = Docente.objects.all()
    return render(request, 'docentes/docente.html', {'docentes': docentes})

@login_required
@user_passes_test(lambda u: u.id_rol.name != "Panol")
def addDocente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('docente')
    else:
        form = DocenteForm()
    return render(request,'docentes/formdocente.html',{'form':form})

@login_required
@user_passes_test(lambda u: u.id_rol.name != "Panol")
def modDocente(request, id):
    docente = Docente.objects.get(pk=id)

    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('docente')
    else:
        form = DocenteForm(instance=docente)
    return render(request,'docentes/formdocente.html',{'form':form})

@login_required
@user_passes_test(lambda u: u.id_rol.name != "Panol")
def delDocente(request, id):
    docente = Docente.objects.get(pk=id)
    docente.delete()
    return redirect('docente')

#CRUD Materiales
@login_required
@user_passes_test(lambda u: u.id_rol.name != "Panol")
def material(request):
    materiales = Material.objects.all()
    return render(request, 'material/material.html', {'materiales': materiales})

@login_required
@user_passes_test(lambda u: u.id_rol.name != "Panol")
def addMaterial(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('material')
    else:
        form = MaterialForm()
    return render(request,'material/formmaterial.html',{'form':form})

@login_required
@user_passes_test(lambda u: u.id_rol.name != "Panol")
def modMaterial(request,id):
    materiales = Material.objects.get(pk=id)

    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=materiales)
        if form.is_valid():
            form.save()
            return redirect('material')
    else:
        form = MaterialForm(instance=materiales)
    return render(request,'material/formmaterial.html',{'form':form})

@login_required
@user_passes_test(lambda u: u.id_rol.name != "Panol")
def delMaterial(request,id):
    materiales = Material.objects.get(pk=id)
    materiales.delete()
    return redirect('material')

#CRUD Prestamo
@login_required
@user_passes_test(lambda u: u.id_rol.name != "Administrador")
def prestamo(request):
    prestamos = AsignarPrestamo.objects.all()
    return render(request, 'prestamo/prestamo.html',{'prestamos':prestamos})

@login_required
@user_passes_test(lambda u: u.id_rol.name != "Administrador")
def addPrestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        
        if form.is_valid():
            material = form.cleaned_data.get('id_material')
            cantidad_solicitada = form.cleaned_data.get('cantidad')
            
            material_obj = Material.objects.get(id=material.id)

            if material_obj.stock < cantidad_solicitada:
                messages.error(request, f'No hay suficiente stock de {material_obj.nombre}. Solo hay {material_obj.stock} unidades disponibles.')
                return redirect('addPrestamo')

            prestamo = form.save(commit=False)
            prestamo.estado = 1 
            prestamo.save()

            material_obj.stock -= cantidad_solicitada  
            material_obj.save()

            messages.success(request, 'Préstamo registrado con éxito.')
            return redirect('prestamo')
    else:
        form = PrestamoForm()

    return render(request, 'prestamo/formprestamo.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.id_rol.name != "Administrador")
def finalizarPrestamo(request, prestamo_id):
    prestamo = get_object_or_404(AsignarPrestamo, id=prestamo_id)
    material = prestamo.id_material
    
    if prestamo.estado == 1: 
        prestamo.estado = 0
        prestamo.save()

        material.stock += prestamo.cantidad
        material.save()

        messages.success(request, f'Préstamo de {material.nombre} finalizado correctamente.')
    else:
        messages.error(request, 'Este préstamo ya ha sido finalizado.')

    return redirect('prestamo')
