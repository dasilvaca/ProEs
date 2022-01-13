from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Signatures(TemplateView):
    template_name = "signatures/signatures.html" #"about.html"