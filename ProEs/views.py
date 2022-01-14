from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

def Home(request):
    """List existing posts."""
    return render(request, 'ProEs/home.html')

def Login_Students(request):
    return render(request, 'ProEs/login_students.html')

