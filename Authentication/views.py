from django.shortcuts import render
from django.http import HttpResponseRedirect

from Authentication.forms import *
from django.contrib.auth import authenticate, login, logout


def login_page(request):
    """"авторизация пользователя"""
    errors = []
    if request.method == 'POST':
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/')
                else:
                    errors += ["disabled account!"]
            else:
                errors += ["Invalid username or password!"]
    else:
        form = AuthorizationForm()

    return render(request,
                  'Registration/authorization_page.html',
                  {'form': form,
                   'errors': errors,
                  })

def logout_page(request):
    """выход из аккаунта"""
    logout(request)
    return render(request, 'UserProfile/home.html')


def registration_page(request):
    """регистрация"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/reg/login/')
    else:
        form = RegistrationForm()
    return render(request, 'Registration/registration_page.html', {'form': form})


def information_page(request):
    """информация о ползователе"""

    user_info = UserInfo.objects.get(user=request.user)

    if request.method == 'POST':
        if user_info:
            form = InformationForm(request.POST, request.FILES, instance=user_info)
        else:
            form = InformationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/')
        else:
            return render(request, 'Registration/user_info_page.html', {'form': form})

    else:
        if user_info:
            form = InformationForm(instance=user_info)
        else:
            form = InformationForm()
    return render(request, 'Registration/user_info_page.html', {'form': form})
