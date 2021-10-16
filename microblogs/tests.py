from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import User

# Create your tests here.

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            '@bardia',
            first_name = 'bard',
            last_name = 'rok',
            email = 'brokhzadifar@gmail.com',
            password = 'password123321',
            bio = 'hello there!'
        )
        self._assert_user_is_valid()


    def test_user_name_cannot_be_empty(self):
        self.user.username = ''
        self._assert_user_is_invalid()

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except(ValidationError):
            self.fail('Test user should be valid')

    def _assert_user_is_invalid(self):
        # we are trying to catch it using with.
        with self.assertRaises(ValidationError):
            self.user.full_clean()

        