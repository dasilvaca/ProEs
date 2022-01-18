from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from apps.usuario2.forms import RegistroForm

# Create your views here.

class RegistrarUsuario(CreateView):
    model = User
    template_name = 'usuario2/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('testview')

def testview(request):
    return render(request, 'base/base2.html')
