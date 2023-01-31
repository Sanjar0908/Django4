from django.shortcuts import render, redirect
from users.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User


def auth_view(request):
    if request.method == 'GET':
        return render(request, 'users/login.html', context={'form': LoginForm})

    elif request.method == 'POST':
        form = LoginForm(data=request.POST)
        """ authenticate user """

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/products/')
            else:
                form.add_error('username', 'chuvak dagy bir jolu poprobuy')

        return render(request, 'users/login.html', context={
            'form': form
        })


def logout_view(request):
    logout(request)
    return redirect('/products/')


def register_view(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }
        return render(request, 'users/register.html', context=context)

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            password1, password2 = form.cleaned_data.get('password1'), form.cleaned_data.get('password2')
            if password1 == password2:
                User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                return redirect('/users/login/')
            else:
                form.add_error('password1', 'ошибка!')

        return render(request, 'users/register.html', context={
            'form': form
        })


