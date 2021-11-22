from django.urls import reverse
from django.test import TestCase
from microblogs.forms import SignUpForm

class SignUpViewTestCase(TestCase):
    pass

    def setUp(self):
        self.url = reverse('sign_up')
        self.form_input = {
            'first_name' : 'Jane',
            'last_name' : 'Doe',
            'username' : '@janedoe',
            'email' : 'janedoe@example.org',
            'bio' : 'my bio',
            'new_password' : 'Password123',
            'password_confirmation' : 'Password123'
        }

    def test_sign_up_url(self):
        self.assertEqual(reverse('sign_up'), '/sign_up/')

    def test_get_sign_up(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertFalse(form.is_bound)

    def test_unsseccessful_sign_up(self):
        self.form_input['username'] = 'BAD_username'
        response = self.client.post(self.url , self.form_input)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertTrue(form.is_bound)

    

