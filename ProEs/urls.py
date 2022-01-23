"""ProEs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path

from ProEs import views as local_views

#Classes for the login and others
from django.contrib.auth.views import LoginView, LogoutView,\
PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('xd/', include('xd.urls')),
    path('admin/', admin.site.urls),

    path('users/', include('users.urls'), name='users'),

    path('courses/', include('courses.urls'), name='courses'),

    path('', local_views.Home),
    path('students', local_views.Login_Students),
    path('recovery', local_views.Recovery_Password),
    path('notes', local_views.Notes),

    #Links for login and others
    path('usuario/', include('apps.usuario2.urls'),name='usuario'),
    path('login/',LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),

    path('reset/password_reset', PasswordResetView.as_view(template_name='ProEs/recovery_password.html'), name="password_reset"),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path('reset/password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/password_reset/done', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),


]
