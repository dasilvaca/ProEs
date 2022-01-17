from django.contrib import admin
from django.urls import include, path

from apps.usuario2.views import RegistrarUsuario

urlpatterns = [
    #Links for login and others
    path('registrar',RegistrarUsuario.as_view(),name='registrar')
]