from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput
from django.test import TestCase
from microblogs.models import User
from microblogs.forms import SignUpForm
from django.urls import reverse
from django.contrib.auth.hashers import check_password

class SignUpsFormTestCase(TestCase):

    def setUp(self):
        self.form_input = {
            'first_name' : 'Jane',
            'last_name' : 'Doe',
            'username' : '@janedoe',
            'email' : 'janedoe@example.org',
            'bio' : 'my bio',
            'new_password' : 'Password123',
            'password_confirmation' : 'Password123'
        }
        form = SignUpForm(data=self.form_input)
        self.assertTrue(form.is_valid())


    def test_valid_sign_up_form(self):
        form = SignUpForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    # neccessary fields
    # assertIn checks if an attribute is in a form or not
    def test_form_has_necessary_fields(self):
        form = SignUpForm()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('username', form.fields)
        self.assertIn('email', form.fields)
        email_field = form.fields['email']
        self.assertTrue(isinstance(email_field, forms.EmailField))
        self.assertIn('bio', form.fields)
        self.assertIn('new_password', form.fields)
        new_password_widget = form.fields['new_password'].widget
        self.assertTrue(isinstance(new_password_widget, forms.PasswordInput))
        self.assertIn('password_confirmation', form.fields)
       
    # form user model validation
    def test_form_uses_model_validation(self):
        self.form_input['username'] = 'badusername'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())


    # password test
    def test_password_must_contain_uppercase_character(self):
        self.form_input['new_password'] = 'badpass123'
        self.form_input['password_confirmation'] = 'badpass123'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())


    # password test
    def test_password_must_contain_lowercase_character(self):
        self.form_input['new_password'] = 'BADPASS123'
        self.form_input['password_confirmation'] = 'BADPASS123'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    
    # password test
    def test_password_must_contain_number(self):
        self.form_input['new_password'] = 'badPASSWW'
        self.form_input['password_confirmation'] = 'badPASSWW'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    #new password and confirmation are the same
    def test_new_password_and_confirmation_are_the_same(self):
        self.form_input['new_password'] = 'Wrongpassword123'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    
    def test_form_save_correctly(self):
        form = SignUpForm(data=self.form_input)
        before_count = User.objects.count()
        form.save()
        after_count = User.objects.count() 
        self.assertEqual(after_count, before_count+1)
        user = User.objects.get(username = '@janedoe')
        self.assertEqual(user.first_name, 'Jane')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'janedoe@example.org')
        self.assertEqual(user.bio, 'my bio')
        is_password_correct = check_password('Password123', user.password)
        self.assertTrue(is_password_correct)



    


    
