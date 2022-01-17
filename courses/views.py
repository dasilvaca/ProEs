from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Courses(TemplateView):
    template_name = "courses/courses.html" #"about.html"

class TopWorst(TemplateView):
    template_name = "courses/topworst.html" #"about.html"

class TopBest(TemplateView):
    template_name = "courses/topbest.html" #"about.html"

class NewCourse(TemplateView):
    template_name = "courses/newcourse.html" #"about.html"

class Spreadsheet(TemplateView):
    template_name = "courses/spreadsheet.html" #"about.html"