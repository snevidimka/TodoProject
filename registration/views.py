from django.shortcuts import render, reverse, redirect
from registration.forms import CustomUserForm
from registration.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='registration/login/')
def create_user(request):
    """ Создание пользователя """
    form = CustomUserForm()

    if request.method == 'POST':
        form = CustomUserForm(data=request.POST)
        success_url = reverse('registration:login')

        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'registration.html', {'form': form})


@login_required(login_url='registration/login/')
def login_view(request):
    """ Залогинивание пользователя """
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        success_url = reverse('main:main')

        if form.is_valid():
            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user and user.is_active:
                login(request, user)
                return redirect(success_url)

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """ Разлогинивание пользователя """
    logout(request)
    success_url = reverse('registration:login')
    return redirect(success_url)
