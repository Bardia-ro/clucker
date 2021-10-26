from django.core.exceptions import ValidationError
from django.test import TestCase
from microblogs.forms import PostForm
from microblogs.models import Post, User


class PostTestCase(TestCase):
    
    def setUp(self):
        userOne = self._create_user()
        self.post_input = {
            'author': userOne,
            'text' : 'posted'
        }


    def test_text_is_not_blank(self):
        self.post_input['text'] = ''
        post = PostForm(data=self.post_input)
        self.assertFalse(post.is_valid())

    def test_author_is_not_blank(self):
        self.post_input['author'] = ''
        post = PostForm(data=self.post_input)
        self.assertFalse(post.is_valid())


    def test_text_is_not_more_than_280(self):
        self.post_input['text'] = '' * 281
        post = PostForm(data=self.post_input)
        self.assertFalse(post.is_valid())

    
    def _create_user(self):
        user = User.objects.create_user(
            username = '@bardia',
            first_name = 'bard',
            last_name = 'rok',
            email = 'brokhzadifr@gmail.com',
            password = 'password123321',
            bio = 'hello there!'
        )
        return user

        
    