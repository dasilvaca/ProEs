from django.contrib import admin
from django.urls import include, path

from apps.usuario2.views import RegistrarUsuario, testview

from django.contrib.auth.decorators import login_required

urlpatterns = [
    #Links for login and others
    path('registrar',RegistrarUsuario.as_view(),name='registrar'),

    #for test
    path('test',login_required(testview),name='testview'),
]
