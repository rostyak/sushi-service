from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import MinValueValidator

from sushi.models import Cook, Dish


class CookCreationForm(UserCreationForm):
    MIN_YEARS_OF_EXPERIENCE = 0

    years_of_experience = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(MIN_YEARS_OF_EXPERIENCE)]
    )

    class Meta:
        model = Cook
        fields = ("username", "first_name", "last_name", "years_of_experience")


class CookYearsOfExperienceUpdateForm(forms.ModelForm):

    class Meta:
        model = Cook
        fields = ("years_of_experience",)

    years_of_experience = forms.IntegerField(
        required=True,
        min_value=0
    )


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by username.. 🔎"
        })
    )


class DishCreateForm(forms.ModelForm):

    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by name.. 🔎"
        })
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by name.. 🔎"
        })
    )