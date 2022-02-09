from django.urls import path

# from . import views

from courses import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.Courses, name = "courses"),
    path("topworst", views.TopWorst, name = "topworst"),
    path("topbest", views.TopBest, name = "topbest"),
    path("newcourse", views.NewCourse, name = "newcourse"),
    path("spreadsheet/<str:id>/", views.Spreadsheet, name = "spreadsheet"),
    path("delete_course/<str:id>/", views.delete_course, name = "delete_course"),
]