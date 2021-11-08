
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from .forms import UserSignupForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def signup(request):
    form = UserSignupForm()

    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for" + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, username)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incoorect')

    return render(request, 'registration/login.html')


def logoutuser(request):

    logout(request)
    return redirect('login')


def profile(request):

    return render(request, 'registration/index.html')
