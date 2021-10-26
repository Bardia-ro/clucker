from django.core.exceptions import ValidationError
from django.test import TestCase
from microblogs.models import User
from microblogs.forms import SignUpForm

class SignUpsFormTestCase(TestCase):



    def test_valid_sign_up_form(self):
        form_input = {
            'first_name' : 'Jane',
            'last_name' : 'Doe',
            'username' : '@janedoe',
            'email' : 'janedoe@example.org',
            'bio' : 'my bio',
            'new_password' : 'password123',
            'password_confirmation' : 'password123'
        }
        form = SignUpForm(data=form_input)
        self.assertTrue(form.is_valid())

    