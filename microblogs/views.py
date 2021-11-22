from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import User

from microblogs.forms import LogInForm, PostForm, SignUpForm

def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('feed')
    #error message
        messages.add_message(request, messages.ERROR, "The username or password entered incorrectly!")
    form = LogInForm()
    return render(request, 'log_in.html' , {'form' : form})

def log_out(request):
    logout(request)
    return redirect('home')

def feed(request):
    postform = PostForm()
    return render(request, 'feed.html', {'form' : postform})

def home(request):
    return render(request, 'home.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request ,user)
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form':form})

def user_list(request):
    users_list = User.objects.all()
    return render(request, 'user_list.html' , {'users_list' : users_list})

def show_user(request ,user_id):
    user = User.objects.get(pk = user_id)
    return render(request, 'show_user.html', {'users' : user})





