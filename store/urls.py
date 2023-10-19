# Description: URL Configuration for store app
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
