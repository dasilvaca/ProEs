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
    salida = db.find({"profesor":profesor})

    for x in salida:
       asignaturas.append(x)

    print(asignaturas)

    # id = str(db.find_one({"asignatura.nombre":"ESTADÍSTICA"},{"_id":1})["_id"])
    # out = db.find_one({"_id":ObjectId(id)})
    return render(request, "courses/courses.html", {"contexto": asignaturas})  # "about.html"


class TopWorst(LoginRequiredMixin, TemplateView):
    template_name = "courses/topworst.html"  # "about.html"


class TopBest(LoginRequiredMixin, TemplateView):
    template_name = "courses/topbest.html"  # "about.html"

@login_required
def NewCourse(request):

    #Para saber las asignaturas de un profesor
    profesor = request.user.username
    asignaturas = []
    db = connect("proesCol")
    #salida = db.find({"profesor":profesor})
    #for x in salida:
     #   asignaturas.append(x["asignatura"]["nombre"])

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
    return render(request, "courses/newcourse.html",{"contexto":asignaturas})  # "about.html"


def Spreadsheet(request, id):
    return render(request, "courses/spreadsheet.html")   # "about.html"
