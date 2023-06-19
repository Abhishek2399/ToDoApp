from django.contrib import admin
from django.urls import path
from . import views

app_name = "ToDoApp"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("add_task/", views.add_task, name="add_task"),
    path("edit_task/<str:pk>", views.edit_task, name="edit_task"),
    path("delete_task/<str:pk>", views.delete_task, name="delete_task"),
]
