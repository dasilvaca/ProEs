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

urlpatterns = [
    # path('xd/', include('xd.urls')),
    path('admin/', admin.site.urls),

    path('users/', include(('users.urls', 'users'), namespace='users')),

    path('courses/', include(('courses.urls', 'courses'), namespace='courses')),

    path('', local_views.Home),
    path('students', local_views.Login_Students),
    path('recovery', local_views.Recovery_Password),
    path('notes', local_views.Notes),

]
