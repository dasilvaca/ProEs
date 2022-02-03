from django.shortcuts import render


from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import *
from users.forms import RegistroForm
from django.contrib import messages

# Create your views here.

class RegistrarUsuario(CreateView):
    model = User
    template_name = 'users/signup.html'
    form_class = RegistroForm
    post_reset_login = True
    
    def get_success_url(self):
        username = self.object.first_name
        mensaje = 'Bienvenido ' + username
        messages.success(self.request, mensaje)
        return reverse('courses')

#No borrar por favor, es para hacer pruebas
def testview(request):
    return render(request, 'common/base_users.html')