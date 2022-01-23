from django.urls import path

# from . import views

from users import views

from users.views import RegistrarUsuario, testview
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('signup',RegistrarUsuario.as_view(),name='signup'),

    #for test
    path('test',testview,name='testview'),
]