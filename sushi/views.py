from django.shortcuts import render
from django.views import generic

from sushi.models import Cook, Dish, DishType


def index(request):
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
    }

    return render(request, "sushi/index.html", context=context)


class CookListView(generic.ListView):
    model = Cook
    template_name = "sushi/cook_list.html"
    context_object_name = "cook_list"
    paginate_by = 10


class CookDetailView(generic.DetailView):
    model = Cook


class DishListView(generic.ListView):
    model = Dish
    template_name = "sushi/dish_list.html"
    context_object_name = "dish_list"
    paginate_by = 10


class DishDetailView(generic.DetailView):
    model = Dish


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "sushi/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 10

