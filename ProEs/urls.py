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

    path('', local_views.Home.as_view(), name = 'home'),
    path('students', local_views.LoginStudents, name = 'login_students'),
    path('notes', local_views.Notes.as_view(), name = 'notes'),
    path('reports/<str:id>/', local_views.reports, name = 'reports'),

    #Links for login and others
    
    
    path('login/',LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),

    path('reset/password_reset', local_views.PasswordResetView.as_view(), name="password_reset"),
    path('reset/password_reset/<uidb64>/<token>/', local_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 
]
