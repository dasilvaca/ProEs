from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#Para conectarse a mongoDB desde python
from utils import *

# Create your views here.
class Courses(LoginRequiredMixin, TemplateView):
    template_name = "courses/courses.html"  # "about.html"


class TopWorst(LoginRequiredMixin, TemplateView):
    template_name = "courses/topworst.html"  # "about.html"


class TopBest(LoginRequiredMixin, TemplateView):
    template_name = "courses/topbest.html"  # "about.html"

@login_required
def NewCourse(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        min = float(request.POST["min"])
        max = float(request.POST["max"])
        query = {"nombre":nombre,"min":min,"max":max}
        db = connect("proesCol")
        db.insert(query)
        #import pdb;pdb.set_trace()
    return render(request, "courses/newcourse.html")  # "about.html"


class Spreadsheet(LoginRequiredMixin, TemplateView):
    template_name = "courses/spreadsheet.html"  # "about.html"
