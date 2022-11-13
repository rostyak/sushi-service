from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from sushi.forms import CookCreationForm, CookYearsOfExperienceUpdateForm, \
    DishCreateForm, CookSearchForm, DishSearchForm
from sushi.models import Cook, Dish, DishType


def index(request):
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    num_visits = request.session.get("num_visits", 1)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits
    }

    return render(request, "sushi/index.html", context=context)


class CookListView(generic.ListView):
    model = Cook
    template_name = "sushi/cook_list.html"
    context_object_name = "cook_list"
    paginate_by = 7
    queryset = Cook.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = CookSearchForm(
            initial={"username": username}
        )

        return context

    def get_queryset(self):
        form = CookSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )

        return self.queryset


class CookDetailView(generic.DetailView):
    model = Cook


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookYearsOfExperienceUpdateForm
    success_url = reverse_lazy("sushi:cooks-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("sushi:cooks-list")


class DishListView(generic.ListView):
    model = Dish
    template_name = "sushi/dish_list.html"
    context_object_name = "dish_list"
    paginate_by = 7
    queryset = Dish.objects.all().select_related("dish_type")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishSearchForm(
            initial={"name": name}
        )

        return context

    def get_queryset(self):
        form = DishSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


class DishDetailView(generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishCreateForm
    success_url = reverse_lazy("sushi:dishes-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishCreateForm
    success_url = reverse_lazy("sushi:dishes-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("sushi:dishes-list")


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "sushi/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 7


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("sushi:dish-types-list")
    template_name = "sushi/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("sushi:dish-types-list")
    template_name = "sushi/dish_type_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("sushi:dish-types-list")
    template_name = "sushi/dish_type_confirm_delete.html"
