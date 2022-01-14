from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Signatures(TemplateView):
    template_name = "signatures/signatures.html" #"about.html"

class TopWorst(TemplateView):
    template_name = "signatures/topworst.html" #"about.html"

class TopBest(TemplateView):
    template_name = "signatures/topbest.html" #"about.html"

class NewSignature(TemplateView):
    template_name = "signatures/newsignature.html" #"about.html"