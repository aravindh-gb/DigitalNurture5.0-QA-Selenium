from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.course_list, name="course_list"),

    path(
        "<int:course_id>/",
        views.course_detail,
        name="course_detail",
    ),
]
urlpatterns = [
    path("", views.course_list, name="course_list"),

    path(
        "<int:course_id>/",
        views.course_detail,
        name="course_detail",
    ),

    path(
        "create/",
        views.course_create,
        name="course_create",
    ),
    path("<int:course_id>/edit/", views.course_update, name="course_update"),
    path(
    "<int:course_id>/delete/",
    views.course_delete,
    name="course_delete",
),

path("register/", views.register, name="register"),
]