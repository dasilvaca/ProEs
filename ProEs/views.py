# Create your views here.
from django.views.generic import TemplateView
from django.urls import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordResetView, PasswordResetConfirmView

#Para conectar con atlas
from utils import *
from bson import ObjectId

class Home(TemplateView):
    template_name = 'ProEs/home.html'


def LoginStudents(request):
    if request.method == 'POST':
        salidaArr = []
        di = request.POST["di"]
        db = connect("proesCol")
        query ={"estudiantes.di":di}
        salida = db.find(query,{"_id":0})
        for i in range(salida.count()):
            salidaArr.append(salida[i])
            estudiantesList = salida[i]["estudiantes"]
            aux = {}
            for j in estudiantesList:
                if j["di"] ==di:
                    aux=j
            salidaArr[i]["estudiantes"] = aux
        return render(request,'ProEs/notes.html',{"contexto":salidaArr})    
    return render(request,'ProEs/login_students.html')


class Notes(TemplateView):
    template_name = 'ProEs/notes.html'


class PasswordResetView(PasswordResetView):
    template_name = "ProEs/recovery_password.html"

    def get_success_url(self):
        messages.success(self.request, "Se envio el link a tu correo!")
        return reverse('home')


class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    post_reset_login = True

    def get_success_url(self):
        messages.success(self.request, 'Contraseña reestablecida correctamente')
        return reverse('courses')

