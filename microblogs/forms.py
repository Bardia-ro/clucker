from django import forms
from django.forms import widgets
from .models import Post, User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name' , 'last_name', 'username','email', 'bio']
        widgets = { 'bio': forms.Textarea() }

    new_password = forms.CharField(label='Password' , widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label='Password confirmation' , widget=forms.PasswordInput())

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        ordering = ['created_at']
        fields = ['author', 'text']
        widgets = {'text': forms.Textarea()}


class LogInForm(forms.Form):
        username = forms.CharField(label="Username")
        password = forms.CharField(label = "Password", widget=forms.PasswordInput())
