from django.contrib import admin
from django.urls import path, include

from sushi.views import index, CookListView, DishListView

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cooks-view"),
    path("dishes/", DishListView.as_view(), name="dishes-view")
]

app_name = "sushi"
