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
        salidaArr1 = []
        di = request.POST["di"]
        db = connect("proesCol")
        query ={"estudiantes.di":di}
        salida = db.find(query,{"_id":0})
        for i in range(salida.count()):
            salidaArr1.append(salida[i])
            estudiantesList = salida[i]["estudiantes"]
            aux = {}
            for j in estudiantesList:
                if j["di"] ==di:
                    aux=j
            salidaArr1[i]["estudiantes"] = aux
        salidaArr2 = []
        for i in range(len(salidaArr1)):
            general_dict={
                "di":salidaArr1[i]["estudiantes"]["di"],
                "asignatura": salidaArr1[i]["asignatura"],
            }
            arrNotas = []
            
            for j in range(len(salidaArr1[i]["tipo_notas"])):
                arrNotas.append({
                    "tipo":salidaArr1[i]["tipo_notas"][j],
                    "nota":int(salidaArr1[i]["estudiantes"]["notas"][j])
                })
            general_dict["notas"]=arrNotas
            general_dict["definitiva"]=salidaArr1[i]["estudiantes"]["definitiva"]
            salidaArr2.append(general_dict)  
        return render(request,'ProEs/notes.html',{"contexto":salidaArr2})    
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

