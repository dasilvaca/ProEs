from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class Login(TemplateView):
    template_name = "users/login.html" #"about.html"

class Signup(TemplateView):
    template_name = "users/signup.html"  # "about.html"