from django.contrib import admin
from django.urls import path, include

from sushi.views import index, CookListView, DishListView

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
]

app_name = "sushi"
