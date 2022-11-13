from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from sushi.models import DishType, Dish, Cook

DISH_TYPE_URL = reverse("sushi:dish-types-list")
DISH_URL = reverse("sushi:dishes-list")
COOK_URL = reverse("sushi:cooks-list")


class PublicDishTypeTests(TestCase):
    def test_login_is_not_required(self):
        response = self.client.get(DISH_TYPE_URL)

        self.assertEqual(response.status_code, 200)


class PrivateDishTypeTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password1213412",
            years_of_experience=5
        )
        self.client.force_login(self.user)

    def test_create_dish_type(self):
        response = self.client.get(reverse("sushi:dish-type-create"))

        self.assertEqual(response.status_code, 200)


class PublicDishTests(TestCase):
    def test_login_is_not_required(self):
        response = self.client.get(DISH_URL)

        self.assertEqual(response.status_code, 200)


class PrivateDishTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password1213412",
            years_of_experience=7
        )
        self.client.force_login(self.user)

    def test_create_dish(self):
        response = self.client.get(reverse("sushi:dish-create"))

        self.assertEqual(response.status_code, 200)


class PublicCookTests(TestCase):
    def test_login_required(self):
        response = self.client.get(COOK_URL)

        self.assertEqual(response.status_code, 200)


class PrivateDriverTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password1213412",
            years_of_experience=7
        )
        self.client.force_login(self.user)

    def test_create_driver(self):
        response = self.client.get(reverse("sushi:cook-create"))

        self.assertEqual(response.status_code, 200)
