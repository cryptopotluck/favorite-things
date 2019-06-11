from django.shortcuts import render, redirect
from user.models import Users
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfilePictureUpdateForm, FirstNameUpdateForm, LastNameUpdateFrom


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome back!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'user/login.html')


def register(request):
    if request.method == 'POST':
        # Get form values
        email = request.POST['email']
        username = request.POST['userName']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Ceck if passwords match

        if password == password2:
            # check username
            if Users.objects.filter(user__username=username).exists():
                messages.error(request, 'We have a copycat, username has been taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already in use try recovering password.')
                    return redirect('register')
                else:
                    # looks good
                    user = User.objects.create_user(email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in please enhance your profile.')
                    return redirect('index')

        else:
            messages.error(request, 'We have a Bad Typer... Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'user/signup.html')


def profile(requests):
    return render(requests, 'user/profile.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You logged out, see you next time!')
        return redirect('login')
