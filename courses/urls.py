from django.urls import path

# from . import views

from courses import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.Courses.as_view(), name = "courses"),
    path("topworst", views.TopWorst.as_view(), name = "topworst"),
    path("topbest", views.TopBest.as_view(), name = "topbest"),
    path("newcourse", views.NewCourse.as_view(), name = "newcourse"),
    path("spreadsheet", views.Spreadsheet.as_view(), name = "spreadsheet"),
]