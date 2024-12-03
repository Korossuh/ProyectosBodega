from django.urls import path
from .views import *

urlpatterns = [
    path('usuarios/', index, name="usuarios"),
    path('usuarios/agregar_usuarios', agregar_usuario, name='agregar_usuario'),
    path('usuarios/editar_usuario/<int:id>/', editar_usuario, name='editar_usuario'),
   path('usuarios/eliminar_usuario/<int:id>/', eliminar_usuario, name='eliminar_usuario'),
]