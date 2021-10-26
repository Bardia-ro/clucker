from django.core.exceptions import ValidationError
from django.test import TestCase
from microblogs.models import User

# Create your tests here.

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username = '@bardi',
            first_name = 'bard',
            last_name = 'rok',
            email = 'brokhzadifar@gmail.com',
            password = 'password123321',
            bio = 'hello there!'
        )
        self._assert_user_is_valid()

    def test_user_name_cannot_be_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid()

    
    def test_username_must_be_unique(self):
        second_user = self._create_second_user()
        self.user.username = second_user.username
        self._assert_user_is_invalid()



    def test_lastname_does_not_have_to_be_unique(self):
        second_user = self._create_second_user()
        self.user.last_name = second_user.last_name
        self._assert_user_is_valid()

    def test_firstname_does_not_have_to_be_unique(self):
        second_user = self._create_second_user()
        self.user.first_name = second_user.first_name
        self._assert_user_is_valid()
    

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except(ValidationError):
            self.fail('Test user should be valid')

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()


    def test_username_starts_with_at_sign(self):
        self.user.username = 'bardia'
        self._assert_user_is_invalid()



    def test_username_must_have_alphanumerical_after_at(self):
        self.user.username = '@bard!ia'
        self._assert_user_is_invalid()


    def test_username_must_have_have_atleast_3_chars(self):
        self.user.username = '@br'
        self._assert_user_is_invalid()


    def test_username_must_have_only_one_at(self):
        self.user.username = '@@bardia'
        self._assert_user_is_invalid()


    def test_first_name_cannot_be_blank(self):
        self.user.first_name = ''
        self._assert_user_is_invalid()


    def test_last_name_cannot_be_blank(self):
        self.user.last_name = ''
        self._assert_user_is_invalid()


    def test_first_name_not_more_than_50(self):
        self.user.first_name = '' * 51
        self._assert_user_is_invalid()

    def test_email_must_not_have_more_than_one_at(self):
        self.user.email = 'brokhzadifar@@gmail.com'
        self._assert_user_is_invalid()
    
    
    def test_email_contain_domain(self):
        self.user.email = 'brokhzadifar@@gmail'
        self._assert_user_is_invalid()
    
    def _create_second_user(self):
        user = User.objects.create_user(
            username = '@bardia',
            first_name = 'bard',
            last_name = 'rok',
            email = 'brokhzadifr@gmail.com',
            password = 'password123321',
            bio = 'hello there!'
        )
        return user

                    
        
  
                    


        