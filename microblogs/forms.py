from django.core.validators import RegexValidator
from django import forms
from django.forms import widgets
from .models import Post, User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name' , 'last_name', 'username','email', 'bio']
        widgets = { 'bio': forms.Textarea() }

    new_password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(),
          validators=[RegexValidator(
            regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
            message='password must contain an lowercase character, an uppercase and a number'
         )]
    )
    password_confirmation = forms.CharField(label='Password confirmation' , widget=forms.PasswordInput())

    def clean(self):
        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'confirmation does not match password.')



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        ordering = ['created_at']
        fields = ['author', 'text']
        widgets = {'text': forms.Textarea()}


class LogInForm(forms.Form):
        username = forms.CharField(label="Username")
        password = forms.CharField(label = "Password", widget=forms.PasswordInput())
