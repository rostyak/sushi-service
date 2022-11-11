from django.contrib import admin
from django.urls import path, include

from sushi.views import (
    index,
    CookListView,
    CookDetailView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeListView
)

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types-list")
]

app_name = "sushi"
