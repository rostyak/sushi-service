from django.test import TestCase


from sushi.forms import CookCreationForm


class FormsTests(TestCase):
    def test_cook_creation_form_with_valid_data(self):
        form_data = {
            "username": "User12345",
            "password1": "usertest0987",
            "password2": "usertest0987",
            "years_of_experience": "8",
            "first_name": "User",
            "last_name": "Test"
        }

        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cook_creation_form_with_not_valid_experience(self):
        form_data = {
            "username": "User12345",
            "password1": "usertest0987",
            "password2": "usertest0987",
            "years_of_experience": "-1",
            "first_name": "User",
            "last_name": "Test"
        }

        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
