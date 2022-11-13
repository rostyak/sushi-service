from django.contrib.auth import get_user_model
from django.test import TestCase

from sushi.models import DishType, Dish


class ModelsTest(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Testing dish")

        self.assertEqual(
            str(dish_type), dish_type.name
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="Testing dish")

        dish = Dish.objects.create(
            name="Test",
            description="Nothing",
            price=5.26,
            dish_type=dish_type,
        )

        self.assertEqual(str(dish), dish.name)

    def test_create_cook(self):
        username = "Test1"
        first_name = "Testing"
        last_name = "Testov"
        password = "testing1920"
        years_of_experience = 6

        cook = get_user_model().objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            years_of_experience=years_of_experience
        )

        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertTrue(cook.check_password(password))

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="Testing_user",
            first_name="Test",
            last_name="User",
            years_of_experience=5
        )

        self.assertEqual(
            str(cook), f"{cook.username} ({cook.first_name} {cook.last_name})"
        )