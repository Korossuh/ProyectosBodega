from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.views import LoginView
class login(LoginView):
    template_name = "login.html"
    authentication_form = FormularioLogin

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url: 
            if self.request.user.is_authenticated and self.request.user.id_rol:
                rol_name = self.request.user.id_rol.name 
                
                if rol_name == "Administrador" and next_url == "/inicio/":
                    return next_url

                if rol_name == "Panol" and next_url == "/inicio panol/":
                    return next_url

                if rol_name != "Administrador" and next_url == "/inicio/":
                    return "/inicio panol/"
                if rol_name != "Panol" and next_url == "/inicio panol/":
                    return "/inicio/"

        return super().get_success_url()
