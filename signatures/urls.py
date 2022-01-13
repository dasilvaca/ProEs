from django.urls import path

# from . import views

from signatures import views

urlpatterns = [
    path("", views.Signatures.as_view(), name="signatures"),
]