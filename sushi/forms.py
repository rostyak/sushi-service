from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import MinValueValidator

from sushi.models import Cook


class CookCreationForm(UserCreationForm):
    MIN_YEARS_OF_EXPERIENCE = 0

    years_of_experience = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(MIN_YEARS_OF_EXPERIENCE)]
    )

    class Meta:
        model = Cook
        fields = ("username", "first_name", "last_name", "years_of_experience")
