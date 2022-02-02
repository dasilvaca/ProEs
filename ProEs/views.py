# Create your views here.
from django.views.generic import TemplateView
from django.urls import *
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordResetView, PasswordResetConfirmView


class Home(TemplateView):
    template_name = 'ProEs/home.html'


class LoginStudents(TemplateView):
    template_name = 'ProEs/login_students.html'


class Notes(TemplateView):
    template_name = 'ProEs/notes.html'


class PasswordResetView(PasswordResetView):
    template_name = "ProEs/recovery_password.html"

    def get_success_url(self):
        return reverse('home')


class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    post_reset_login = True

    def get_success_url(self):
        return reverse('courses')
