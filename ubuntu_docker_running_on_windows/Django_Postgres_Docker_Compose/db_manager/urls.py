from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_platform", views.add_platform, name="add_platform"),
    path("add_record_type", views.add_record_type, name="add_record_type"),
]