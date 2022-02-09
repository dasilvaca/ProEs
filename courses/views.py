import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#Para conectarse a mongoDB desde python
from utils import *
from bson import ObjectId
import pymongo
#Cast from str to array
from ast import literal_eval

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


def TopWorst(request):
    #se debe recibir un id en el argumento, cuando esté listo se debe borrar el id de abajo
    #Solo funciona por ahora con una sola materia
    id = '6201dd30cf634ef49138dec8'
    db = connect("proesCol")
    salida = db.find_one({"_id":ObjectId(id)},{"estudiantes":1,"_id":0})["estudiantes"]

    ordered = sorted(salida, key=lambda d: d['definitiva'])
    salidaArr=[]
    
    if len(ordered)> 3:
        salidaArr=[ordered[0],ordered[1],ordered[2]]
    else:
        for i in range(len(ordered)):
            salidaArr.append(ordered[i])
    return render(request,"courses/topworst.html",{"contexto":salidaArr})  # "about.html"


def TopBest(request):
    #se debe recibir un id en el argumento, cuando esté listo se debe borrar el id de abajo
    #Solo funciona por ahora con una sola materia
    id = '6201dd30cf634ef49138dec8'
    db = connect("proesCol")
    salida = db.find_one({"_id":ObjectId(id)},{"estudiantes":1,"_id":0})["estudiantes"]
    
    ordered = sorted(salida, key=lambda d: d['definitiva'], reverse=True)
    salidaArr=[]

    if len(ordered)> 3:
        salidaArr=[ordered[0],ordered[1],ordered[2]]
    else:
        for i in range(len(ordered)):
            salidaArr.append(ordered[i])
    return render(request,"courses/topbest.html",{"contexto":salidaArr})  # "about.html"

@login_required
def NewCourse(request):
    #id = str(db.find_one({"asignatura.nombre":"ESTADÍSTICA"},{"_id":1})["_id"])
    #out = db.find_one({"_id":ObjectId(id)})
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        min = float(request.POST["min"])
        max = float(request.POST["max"])
        profesor = request.user.username
        query = {"asignatura":{"nombre":nombre,"min":min,"max":max},"profesor":profesor,"tipo_notas":[],"estudiantes":{
            "nombre":"",
            "di":"",
            "notas":[],
            "definitiva":0,
        }}
        db = connect("proesCol")
        db.insert(query)
        return redirect('courses')
    return render(request, "courses/newcourse.html")  # "about.html"

@login_required
def Spreadsheet(request, id):
    #tipo_notas y estudiantes es lo que se va a recibir del spreedsheet

    db = connect("proesCol")
    query = {"_id":ObjectId(id)}
    salida= db.find(query)[0]

    if request.method == 'POST':
        estudiantes = literal_eval(request.POST['estudiantes'])
        tipo_notas = literal_eval(request.POST['tipo_notas'])
        if tipo_notas != salida["tipo_notas"]:
            db.update_one(query,{"$set":{"tipo_notas":tipo_notas}})
        if estudiantes != salida["estudiantes"]:
            db.update_one(query,{"$set":{"estudiantes":estudiantes}})
        salida= db.find(query)[0]
    
    salida["id"] = str(salida["_id"])
    return render(request, "courses/spreadsheet.html",{"contexto":salida})   # "about.html"