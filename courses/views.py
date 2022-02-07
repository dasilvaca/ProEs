from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#Para conectarse a mongoDB desde python
from utils import *
from bson import ObjectId

# Create your views here.

@login_required
def Courses(request):
    # Para saber las asignaturas de un profesor
    profesor = request.user.username
    asignaturas = []
    db = connect("proesCol")
    salida = db.find({"profesor":profesor},{"asignatura.nombre":1})
    for x in salida:
        x["id"]=str(x["_id"])
        asignaturas.append(x)
    return render(request, "courses/courses.html", {"contexto": asignaturas})  # "about.html"


class TopWorst(LoginRequiredMixin, TemplateView):
    template_name = "courses/topworst.html"  # "about.html"


class TopBest(LoginRequiredMixin, TemplateView):
    template_name = "courses/topbest.html"  # "about.html"

@login_required
def NewCourse(request):
    #id = str(db.find_one({"asignatura.nombre":"ESTADÍSTICA"},{"_id":1})["_id"])
    #out = db.find_one({"_id":ObjectId(id)})
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        min = float(request.POST["min"])
        max = float(request.POST["max"])
        profesor = request.user.username
        query = {"asignatura":{"nombre":nombre,"min":min,"max":max},"profesor":profesor}
        db = connect("proesCol")
        db.insert(query)
        return redirect('courses')
    return render(request, "courses/newcourse.html")  # "about.html"

@login_required
def Spreadsheet(request, id):
    #tipo_notas y estudiantes es lo que se va a recibir del spreedsheet
    tipo_notas = []
    estudiantes = {}

    db = connect("proesCol")
    query = {"_id":ObjectId(id)}
    salida= db.find(query)[0]
    salida["id"] = str(salida["_id"])
    '''
    if tipo_notas != salida["tipo_notas"]:
        db.update_one(query,{"$set":{"tipo_notas":tipo_notas}})
    if estudiantes != salida["estudiantes"]:
        db.update_one(query,{"$set":{"estudiantes":estudiantes}})
    salida = db.find(query)[0]
    salida["id"] = str(salida["_id"])
    '''
    return render(request, "courses/spreadsheet.html",{"contexto":salida})   # "about.html"