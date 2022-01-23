from django.urls import path

# from . import views

from courses import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(views.Courses.as_view()), name="courses"),
    path("topworst", login_required(views.TopWorst.as_view()), name="topworst"),
    path("topbest", login_required(views.TopBest.as_view()), name="topbest"),
    path("newcourse", login_required(views.NewCourse.as_view()), name="newcourse"),
    path("spreadsheet", login_required(views.Spreadsheet.as_view()), name="spreadsheet"),
]