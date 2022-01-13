from django.urls import path

# from . import views

from signatures import views

urlpatterns = [
    path("", views.Signatures.as_view(), name="signatures"),
    path("topworst", views.TopWorst.as_view(), name="topworst"),
    path("topbest", views.TopBest.as_view(), name="topbest"),
]