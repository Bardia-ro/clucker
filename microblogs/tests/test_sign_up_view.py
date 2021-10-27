from django.urls import reverse
from django.test import TestCase
from microblogs.forms import SignUpForm

class SignUpViewTestCase(TestCase):
    pass

    def test_get_sign_up(self):
        url = reverse('sign_up')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))