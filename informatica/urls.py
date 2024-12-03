from django.contrib import admin
from django.urls import path
from .views import *
from informatica import views

urlpatterns = [
    path("", inicio, name="inicio"),  
    path("inicio/", index, name="index"),
    path('inicio panol/', panol, name="indexpanol"),
    
    #Url para CRUD docente
    path("Docente/", docente, name='docente'),
    path("Agregar Docente/", addDocente, name='addDocente'),
    path('Modificar Docente/<int:id>',views.modDocente, name='modDocente'),
    path('Eliminar Docente/<int:id>',views.delDocente, name='delDocente'),

    #Url para Crud Materiales
    path("Materiales/",material,name='material'),
    path("Agregar Material/",addMaterial,name='addMaterial'),
    path("Modificar Material/<int:id>",views.modMaterial,name='modMaterial'),
    path("Eliminar Material/<int:id>",views.delMaterial,name='delMaterial'),

    #Url Prestamo
    path("Prestamo/",prestamo,name='prestamo'),
    path("Agregar Prestamo/",addPrestamo,name='addPrestamo'),
    path("finalizar Prestamo/<int:prestamo_id>",views.finalizarPrestamo,name='finalizarPrestamo')
]
