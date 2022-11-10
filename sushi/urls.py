from django.contrib import admin
from django.urls import path, include

from sushi.views import index, CookListView

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cooks-view"),
]

app_name = "sushi"
