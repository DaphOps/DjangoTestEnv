from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.contrib import messages
from djangolango.apps.user.models.form import UserRegisterForm
from djangolango.apps.user.models.formlogin import LoginForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, "Invalid username or password")
                return redirect('login')
            messages.success(request, f'Welcome {username}!')
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'user/accounts/profile.html')

@login_required
def logout(request):
    if request.method == "POST":
        return redirect('login')
    return render(request, 'user/logout.html')