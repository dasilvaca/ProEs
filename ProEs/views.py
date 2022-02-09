# Create your views here.
import json
from django.views.generic import TemplateView
from django.views import View
from django.urls import *
from django.shortcuts import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.views import *

#Para conectar con atlas
from utils import *
from bson import ObjectId
import pymongo

#PDfs
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


class Home(TemplateView):
    template_name = 'ProEs/home.html'

def reports(request, username, id):

    def link_callback(uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        result = finders.find(uri)
        if result:
            if not isinstance(result, (list, tuple)):
                result = [result]
            result = list(os.path.realpath(path) for path in result)
            path = result[0]
        else:
            sUrl = settings.STATIC_URL  # Typically /static/
            sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
            mUrl = settings.MEDIA_URL  # Typically /media/
            mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

            if uri.startswith(mUrl):
                path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                return uri

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    template_path = 'ProEs/reports.html'

    db = connect("proesCol")
    query = {"_id":ObjectId(id)}
    salida= db.find(query)[0]

    context = {
        'icon': '{}{}'.format(settings.BASE_DIR, '/static/common/logos/2.png'),
        'contexto':salida,
        'docente': username
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def LoginStudents(request):
    print(settings.BASE_DIR)
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
        salidaArr2 = {"cedula" : di, "materias":salidaArr2}
        return render(request,'ProEs/notes.html', {"contexto" : salidaArr2})
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

