from django.contrib import admin
from django.urls import path, include

from sushi.views import index, CookListView, DishListView, DishTypeListView

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types-list")
]

app_name = "sushi"
