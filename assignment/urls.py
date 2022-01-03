
from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("", views.Indexpage, name = "index-page"),
    path("records/", views.Records, name = "records-page"),
]
    