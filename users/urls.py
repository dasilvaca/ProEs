from django.urls import path

# from . import views

from users import views

urlpatterns = [
    path("login", views.Login.as_view(), name="login"),]