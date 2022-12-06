from django.contrib import admin
from django.urls import path, include

from sushi.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "sushi"
