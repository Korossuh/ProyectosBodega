from django.urls import path 
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", login.as_view(), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]